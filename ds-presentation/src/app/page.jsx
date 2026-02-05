
import { CreditCardProject, HealthCareProject, LoanProject, RetailProject, WorldDataProject } from '@/projectData/CONSTANTS'
import { sluggify } from '@/utils/strTransform'
import Image from 'next/image'
import Link from 'next/link'


function HomePage() {
  const dataArr = [
    { title: CreditCardProject, img: "/project_title_images/credit_card.png" },
    { title: HealthCareProject, img: "/project_title_images/healthcare.jpeg" },
    { title: LoanProject, img: "/project_title_images/loan.jpeg" },
    { title: RetailProject, img: "/project_title_images/retail.jpeg" },
    { title: WorldDataProject, img: "/project_title_images/world.jpeg" },
  ]
  return (
    <div className='home-page'>
      <h2>Projects</h2>
      <Link
        target="_blank"
        className='my-link' href={"https://www.linkedin.com/in/abdulbasit-abdulhakeem-013a42213"}>by Abdulbasit</Link>
      <section className="project-list">
        
        {dataArr.map(({ title, img }) => {
          const sluggifiedTitle = sluggify(title)
          return <Link className='each-project-link' key={sluggifiedTitle} href={`/projects/${sluggifiedTitle}`}>

            <Image width={300} height={300} src={img} alt={title} loading='eager' />
            <h4>  {title} </h4>
          </Link>
        })}
      </section>


    </div>
  )
}

export default HomePage