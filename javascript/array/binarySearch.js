


function binarySearch(arr,target){
    // console.log(arr,target)

    low = 0
    high = arr.length - 1
    mid = Math.floor((low + high) / 2)

    // console.log(low,high,mid)

    while(low <= high){

        mid = Math.floor((low + high) / 2)

        if(arr[mid] == target){
            return mid
        }
        else if(arr[mid] > target){
            high = mid - 1
        }else{
            low = mid + 1
        }
    }

    return -1 
}


console.log(binarySearch([2, 4, 6, 8, 10, 12, 14],10))