<template>
  <div>
    <HeaderComponent />
    <ProductList />
    
  </div>
</template>

<script>
import HeaderComponent from '@/components/Header.vue';
import ProductList from '@/components/ProductList.vue';


export default {
  name: 'HomeView',
  components: {
    HeaderComponent,
    ProductList,
    
  },
};
</script>

<style scoped>
/* Estilos específicos para la vista Home */
</style>