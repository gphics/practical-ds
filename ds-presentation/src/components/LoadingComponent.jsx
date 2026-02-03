

function LoadingComponent({loadingClass ="loading-component"}) {
  return (
      <div className={loadingClass}>
          <div className="spinner">
              <div className="backdrop"></div>
          </div>
    </div>
  )
}

export default LoadingComponent