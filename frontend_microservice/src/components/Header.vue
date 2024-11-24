<template>
    <header>
      <h1>Gestión de Productos y Ventas</h1>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
        </ul>
      </nav>
    </header>
  </template>
  
  <script>
  export default {
    name: 'HeaderComponent',
  };
  </script>
  
  <style scoped>
  /* Estilos específicos para el header */
  header {
    background-color: #42b983;
    color: white;
    padding: 1rem;
  }
  nav ul {
    list-style: none;
    padding: 0;
  }
  nav li {
    display: inline;
    margin-right: 1rem;
  }
  </style>