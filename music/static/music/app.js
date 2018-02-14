var s = $("#status").val();
if (s=='success'){
    $('#myModal').modal('show');
}

function sendData(id){
    $("#btn-delete").attr("href", "delete/"+id);
}