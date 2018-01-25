

function editSong(id){
    var x = '-';
    $.ajax({
        url: '/edit/'+id,
        method: 'GET',
        dataType: 'json',
        success: function(data){
            x = data;
            console.log(data);

            $("#box").val(data);
        }
    });
    console.log("x : ",x);
}