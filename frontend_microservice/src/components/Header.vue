<template>
  <header>
    <h1><router-link to="/">Gestión de Productos y Ventas</router-link></h1>
    <nav>
      <ul>
        <li><router-link to="/productos">Productos</router-link></li>
        <li><router-link to="/ventas">Ventas</router-link></li>
      </ul>
    </nav>
    <div class="loader">
      <div class="cell"></div>
      <div class="cell"></div>
      <div class="cell"></div>
      <div class="cell"></div>
      <div class="cell"></div>
      <div class="cell"></div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'HeaderComponent',
};
</script>

<style scoped>
/* Estilo base */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@500;700&display=swap');

header {
  background-color: #1e272e; /* Fondo gris oscuro */
  color: #ffffff;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #0a0d10;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
}

h1 {
  font-family: 'Roboto', sans-serif;
  font-size: 1.8rem;
  font-weight: 700;
  color: #38d9a9; /* Turquesa */
  margin: 0;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: color 0.3s;
}

h1 a {
  text-decoration: none;
  color: inherit;
}

h1:hover {
  color: #20c997; /* Verde turquesa más oscuro */
}

nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
}

nav li {
  margin-right: 1.5rem;
}

nav a {
  text-decoration: none;
  color: #dcdde1; /* Gris claro */
  font-size: 1rem;
  font-weight: 500;
  transition: color 0.3s, transform 0.2s;
}

nav a:hover {
  color: #38d9a9; /* Turquesa */
  transform: translateY(-3px);
}

/* Loader */
.loader {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: 1.5rem;
}

.cell {
  width: 12px;
  height: 12px;
  background-color: #38d9a9; /* Turquesa uniforme */
  border-radius: 50%;
  animation: bounce 1.5s infinite;
}

.cell:nth-child(1) { animation-delay: 0s; }
.cell:nth-child(2) { animation-delay: 0.2s; }
.cell:nth-child(3) { animation-delay: 0.4s; }
.cell:nth-child(4) { animation-delay: 0.6s; }
.cell:nth-child(5) { animation-delay: 0.8s; }
.cell:nth-child(6) { animation-delay: 1s; }

@keyframes bounce {
  0%, 80%, 100% {
    transform: scale(0.8);
    opacity: 0.6;
  }
  50% {
    transform: scale(1.2);
    opacity: 1;
  }
}
</style>
