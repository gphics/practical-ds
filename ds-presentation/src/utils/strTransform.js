export function sluggify(text) {
    const result = text.toLowerCase().split(" ").join("-")
    return result
}
export function deSluggify(text) {
   
    const result = text.toLowerCase().split("-").join(" ");
    return result
}

