import Image from "next/image"


function ComplexRenderer({ insights }) {
    return (
        <div className='complex-renderer'>

            <h4 className="intro-header big-header">Detailed Insights</h4>
            {insights.map(({ informations, topic }, index) => {
                return <section key={index} className="topic-holder">
                    <h5> {topic} </h5>
                    {informations.map((contents, i) => <InsightRenderer key={i} {...contents} />)}
                </section>
            })}
        </div>
    )
}


function InsightRenderer({ question, answer, imgs = [] }) {
    return <section className="each-insight">
        <p>
            <span>Question</span>
            <br />
            {question}
        </p>
        <p>
            <span>Answer</span>
            <br />
            {answer}
        </p>
        {imgs.length ? <ImgRenderer imgs={imgs} /> : <></>}
    </section>
}

function ImgRenderer({ imgs }) {
    return <div className="graph-holder">
        {imgs.map((imgUrl, index) => <Image quality={100} width={500} height={500} src={imgUrl} alt="graphs" key={index} />)}
    </div>
}

export default ComplexRenderer