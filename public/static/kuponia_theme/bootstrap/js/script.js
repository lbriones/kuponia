
$(document).ready(function() {
    $("#form_envio").validate({
        debug: true,
        submitHandler: function(form) {
            // alert("en summit handler");
            var parametros = {
                "email" : $('#email').val(),
                "nombre" : $('#nombre').val()
            };
            $.ajax({
                data:  parametros,
                url:   'enviarmail.php',
                type:  'post',
                beforeSend: function () {
                    $("#resultado").html("Procesando, espere por favor...");
                    alert("Ya eres parte de Kuponia");
                    
                },
                success:  function (respuesta) {
                    //if(respuesta ==1){
                    //    alert('Mail enviado correctamente');
                    //    
                    //}else if(respuesta == 0){
                    //    alert('No se pudo enviar su registro, vuelva a intentarlo');
                    //}else{
                    //    alert(respuesta);
                    //}
                    //$("#tecu"+codigo_envio).html(response);
          $("#msg").html( respuesta );
          

                }
            });
        }
        ,
        rules: {
            // simple rule, converted to {required:true}
            nombre:   "required"
            email:{
                        required:true,
                        email: true
            }
        }
    });
    

});
