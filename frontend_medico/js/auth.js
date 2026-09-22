document.addEventListener('DOMContentLoaded', () => {
    const formulario = document.querySelector('#formulario-login');
    const mensajeError = document.querySelector('#mensaje-error');
    const botonIngresar = document.querySelector('.boton-ingresar');

    formulario.addEventListener('submit', async (evento) => {
        evento.preventDefault(); // Evita que la página se recargue
        
        // Estado de carga inicial
        mensajeError.textContent = '';
        botonIngresar.disabled = true;
        botonIngresar.textContent = 'Verificando...';

        const correo = document.querySelector('#correo').value.trim();
        const contrasena = document.querySelector('#contrasena').value.trim();

        // 1. Validación de campos vacíos en el frontend
        if (!correo || !contrasena) {
            mostrarError('Por favor, complete todos los campos.');
            restaurarBoton();
            return;
        }

        try {
            /* 
            ========================================================
            CÓDIGO DE PRODUCCIÓN (Descomentar cuando el backend esté listo)
            ========================================================
            const respuesta = await fetch('http://localhost:8000/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ correo: correo, contrasena: contrasena })
            });
            const datos = await respuesta.json();
            
            if (!respuesta.ok) throw new Error(datos.mensaje || 'Error de credenciales');
            
            // Guardar token y redirigir
            localStorage.setItem('token', datos.token);
            window.location.href = 'paginas/dashboard.html';
            */

            // ========================================================
            // SIMULACIÓN TEMPORAL PARA PRUEBAS DE UI
            // ========================================================
            await new Promise(resolve => setTimeout(resolve, 1000)); // Simula delay de red
            
            if (correo === 'doctor@clinica.com' && contrasena === '12345678') {
                window.location.href = 'paginas/dashboard.html';
            } else {
                throw new Error('Credenciales incorrectas. Verifique su correo o contraseña.');
            }

        } catch (error) {
            // 2. Manejo de errores seguro
            mostrarError(error.message || 'Error al conectar con el servidor.');
        } finally {
            restaurarBoton();
        }
    });

    // Funciones auxiliares de una sola responsabilidad
    function mostrarError(mensaje) {
        mensajeError.textContent = mensaje;
    }

    function restaurarBoton() {
        botonIngresar.disabled = false;
        botonIngresar.textContent = 'Iniciar Sesión';
    }
});