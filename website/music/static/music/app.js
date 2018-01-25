

function editSong(id){
    $.ajax({
        url: 'edit/song/'+id,
        type: 'GET',
        dataType: 'json',
        success: function(data){
            console.log("data : ",data);
        },
        error: function(xhr, errMsg, err){
            console.log("xhr : ",xhr);
            console.log("errMsg : ",errMsg);
            console.log("err : ",err);
        }
    });
}