
import { imgUrl } from '@/projectData/CONSTANTS'
import Image from 'next/image'


function SingleProjectPage() {
  return (
    <div>SingleProjectPage
      <Image quality={100} height={400} src={imgUrl} width={400} alt="project img"/>

    </div>
  )
}

export default SingleProjectPage