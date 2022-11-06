$(document).ready(function(){
    $("#btnEliminar").click(function(){
        var resultado = window.confirm('Estas seguro?');
        if (resultado === true) {
            window.alert('Okay, si estas seguro.');
        } else { 
            window.alert('Pareces indeciso');
        }
    });
});

function eliminar() {
    var resultado = window.confirm('Estas seguro?');
    if (resultado === true) {
        window.alert('Okay, si estas seguro.');
    } else { 
        window.alert('Pareces indeciso');
    }
}