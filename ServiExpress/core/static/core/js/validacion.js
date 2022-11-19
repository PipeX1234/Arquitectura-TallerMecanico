$("#formProveedor").validate(
    {
        "rules":
        {
            "idSucursalProveedor":
            {
                required: true
            },
            "nombreProveedor":
            {
                required: true,
                minlength: 2,
                maxlength: 160
            },
            "correoProveedor":
            {
                required: true,
                email: true,
                maxlength: 100,
                minlength: 2
            },
            "telefonoProveedor":
            {
                required: true,
                minlength: 8,
                maxlength: 8
            },
        },
        messages:
        {
            "idSucursalProveedor":
            {
                required: "<br> Debe seleccionar una sucursal"
            },
            "nombreProveedor":
            {
                required: "Debe ingresar un nombre",
                minlength: "El nombre debe estar entre 2 y 160 caracteres",
                maxlength: "El nombre debe estar entre 2 y 160 caracteres"
            },
            "correoProveedor":
            {
                required: "Debe ingresar el correo del proveedor",
                email: "Debe ingresar un correo. Ej: proveedor@dominio.com",
                maxlength: "Debe estar entre 2 y 100 caracteres",
                minlength: "Debe estar entre 2 y 100 caracteres"
            },
            "telefonoProveedor":
            {
                required: "El telefono es un dato obligatorio",
                minlength: "Debe ingresar el número telefonico sin el 9 (En total 8 números)",
                maxlength: "Debe ingresar el número telefonico sin el 9 (En total 8 números)"
            },
        }
    }
)

$("#formLogin").validate(
    {
        "rules":
        {
            "username":
            {
                required: true,
                minlength: 3,
                maxlength: 150
            },
            "password":
            {
                required: true,
                maxlength: 100,
                minlength: 3
            },
        },
        messages:
        {
            "username":
            {
                required: "Debe ingresar un usuario",
                minlength: "El usuario debe estar entre 3 y 150 caracteres",
                maxlength: "El usuario debe estar entre 3 y 150 caracteres"
            },
            "password":
            {
                required: "Debe ingresar su contraseña",
                maxlength: "Debe estar entre 3 y 128 caracteres",
                minlength: "Debe estar entre 3 y 128 caracteres"
            },
        }
    }
)