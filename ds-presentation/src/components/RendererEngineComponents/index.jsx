import ComplexRenderer from "./ComplexRenderer"
import SimpleRenderer from "./SimpleRenderer"


function MainRendererEngine({ data: { title, description, link, insightSummary, insights } }) {
    const simpleData = { title, description, link, insightSummary }
    return (
        <div className="main-engine">
            <SimpleRenderer {...simpleData} />
            <ComplexRenderer insights={insights} />
        </div>
    )
}

export default MainRendererEngine