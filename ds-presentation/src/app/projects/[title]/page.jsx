import MainRendererEngine from "@/components/RendererEngineComponents"
import { deSluggify } from "@/utils/strTransform"
import Image from "next/image"
import Link from "next/link"


async function fetchData(fileName) {
  try {
    const filePath = `../../../projectData/${fileName}`
    const { default: result } = await import(filePath)
    return result
  } catch (error) {
    return error.message
  }

}

async function SingleProjectPage({ params }) {

  // querrying the title from the url
  const { title } = await params

  // normalizing the title
  const originalTitle = deSluggify(title)

  // setting default value
  let dataFileName = ""

  // Matching project title to corresponding data file
  if (originalTitle.includes("credit")) {
    dataFileName = "creditCard.js"
  } else if (originalTitle.includes("health")) {
    dataFileName = "healthCare.js"
  } else if (originalTitle.includes("loan")) {
    dataFileName = "loan.js"
  } else if (originalTitle.includes("retail")) {
    dataFileName = "retail.js"
  } else if (originalTitle.includes("world")) {
    dataFileName = "world.js"
  } else {
    // if no match found
    dataFileName = null
  }

  // fetching data
  const data = await fetchData(dataFileName)

  // checking if data exists
  const dataExist = typeof data === "string" ? false : true


  return (
    <div className="single-project-page">
      {dataExist ? <MainRendererEngine data={data} /> : <section className="not-found-alert">
        <Image height={300} width={300} alt="file not found" src={"/other_visuals/file_not_found.jpeg"} />
        <Link href="/">Back Home</Link>
      </section>}
    </div>
  )
}

export default SingleProjectPage