// function getOrder(start, end) {
//     var length = end - start;
//     var myorder = new Array();
//     var index = 0;
//     while (index < length+1) {
//         var flag = true;
//         var num = index
//         for (var i in myorder) {
//             if (myorder[i] == num) {
//                 flag = false;
//             }
//         }
//         if (flag == true) {
//             myorder[index] = num;
//             index++;
//         }
//     }
//     for(var i in myorder) {
//         myorder[i] = myorder[i] + 1;
//     }
//     return myorder;
// }


function getOrder(start, end) {
    var length = end - start;
    var myorder = new Array();
    var index = 0;
    while (index < length+1) {
        
        var num = index
        myorder[index] = num;
        index++;
    }
    for(var i in myorder) {
        myorder[i] = myorder[i] + 1;
    }
    return myorder;
}

module.exports = getOrder;