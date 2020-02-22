const merge_sort = (function(unsorted){
    if(unsorted.length > 1){
        var mid = Math.floor(unsorted.length/2)
        var left = merge_sort(unsorted.slice(0,mid))
        var right = merge_sort(unsorted.slice(mid,))
        return merge(left, right)
    } else {
        return unsorted
    }
})

const merge = (function(left, right){
    var sorted = []
    while(left.length > 0 && right.length > 0){
        left[0] < right [0] ? sorted.push(left.shift()) : sorted.push(right.shift())
    }
    while(left.length>0){
        sorted.push(left.shift())
    }
    while(right.length>0){
        sorted.push(right.shift())
    }
    return sorted
})

console.log(merge_sort([27, 369, 63, 126, 252, 990, 54, 18]))
