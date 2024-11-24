<template>
  <div>
    <h2>Lista de Productos</h2>
    <ul>
      <li v-for="product in products" :key="product.id">{{ product.name }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ProductList',
  data() {
    return {
      products: [
        { id: 1, name: 'Producto 1' },
        { id: 2, name: 'Producto 2' },
        { id: 3, name: 'Producto 3' },
      ],
    };
  },
};
</script>

<style scoped>
/* Estilos específicos para la lista de productos */
h2 {
  color: #2c3e50;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  background: #f9f9f9;
  margin: 0.5rem 0;
  padding: 0.5rem;
  border: 1px solid #ddd;
}
</style>