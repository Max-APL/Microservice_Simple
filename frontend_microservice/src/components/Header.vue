<template>
  <header>
    <h1>Gestión de Productos y Ventas</h1>
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <!-- Más enlaces de navegación -->
      </ul>
    </nav>
    <!-- Decoración del loader dentro del header -->
    <div class="loader">
      <div class="cell d-0"></div>
      <div class="cell d-1"></div>
      <div class="cell d-2"></div>
      <div class="cell d-1"></div>
      <div class="cell d-2"></div>
      <div class="cell d-2"></div>
      <div class="cell d-3"></div>
      <div class="cell d-3"></div>
      <div class="cell d-4"></div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'HeaderComponent',
};
</script>

<style scoped>
/* Estilos del header */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');

header {
  background-color: #2c3e50; /* Color de fondo oscuro y profesional */
  color: white;
  padding: 1.5rem 3rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2); /* Sombra sutil pero más destacada */
  position: relative;
  border-bottom: 2px solid #1a252f; /* Borde más oscuro */
  border-radius: 12px 12px 0 0;
  width: 100%;
}

/* Título con una tipografía más elegante */
h1 {
  font-family: 'Montserrat', sans-serif; /* Usamos una fuente moderna */
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0;
  color: #ecf0f1; /* Color más suave y profesional */
  letter-spacing: 2px;
  text-transform: uppercase;
  flex-grow: 1;
  transition: color 0.3s ease;
}

h1:hover {
  color: #f39c12; /* Efecto color dorado al pasar el mouse */
}

/* Estilo de la barra de navegación */
nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
}

nav li {
  margin-right: 2.5rem;
}

nav a {
  text-decoration: none;
  color: #ecf0f1; /* Color claro para los enlaces */
  font-size: 1.2rem;
  font-weight: 500;
  transition: color 0.3s ease, transform 0.3s ease; /* Agregar efecto de transición */
}

nav a:hover {
  color: #f39c12; /* Color dorado en hover */
  transform: scale(1.1); /* Aumento de tamaño en hover */
}

/* Estilos para la decoración del loader dentro del header */
.loader {
  --cell-size: 30px;
  --cell-spacing: 4px;
  --cells: 3;
  --total-size: calc(var(--cells) * (var(--cell-size) + 2 * var(--cell-spacing)));
  display: flex;
  flex-wrap: wrap;
  width: var(--total-size);
  height: var(--total-size);
  margin-left: 20px; /* Separar del contenido del header */
}

/* Estilo de las celdas del loader */
.cell {
  flex: 0 0 var(--cell-size);
  margin: var(--cell-spacing);
  background-color: transparent;
  box-sizing: border-box;
  border-radius: 50%;
  animation: 1.5s ripple ease infinite;
}

/* Diferentes colores para cada celda */
.cell.d-1 { animation-delay: 100ms; }
.cell.d-2 { animation-delay: 200ms; }
.cell.d-3 { animation-delay: 300ms; }
.cell.d-4 { animation-delay: 400ms; }

.cell:nth-child(1) { --cell-color: #00FF87; }
.cell:nth-child(2) { --cell-color: #0CFD95; }
.cell:nth-child(3) { --cell-color: #17FBA2; }
.cell:nth-child(4) { --cell-color: #23F9B2; }
.cell:nth-child(5) { --cell-color: #30F7C3; }
.cell:nth-child(6) { --cell-color: #3DF5D4; }
.cell:nth-child(7) { --cell-color: #45F4DE; }
.cell:nth-child(8) { --cell-color: #53F1F0; }
.cell:nth-child(9) { --cell-color: #60EFFF; }

/* Animación ripple */
@keyframes ripple {
  0% {
    background-color: transparent;
  }

  30% {
    background-color: var(--cell-color);
  }

  60% {
    background-color: transparent;
  }

  100% {
    background-color: transparent;
  }
}
</style>
