import Link from 'next/link'


function SimpleRenderer({ title, description, link, insightSummary }) {
    return (
        <div className='simple-renderer'>
            <h3 className='big-header'> {title} </h3>
            <p> {description} </p>
            <p className='data-source-paragraph'>Data Source: <Link href={link}> click here </Link></p>
            <h4 className='big-header'>Summary Of Data Exploration</h4>
            <p>{insightSummary}</p>
        </div>
    )
}

export default SimpleRenderer