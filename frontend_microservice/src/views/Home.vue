<template>
  <HeaderComponent />
  <div class="home-container">
    <!-- Banner Principal -->
    <div class="hero-banner">
      <div class="hero-text">
        <h1>Bienvenido a TechZone</h1>
        <p>Celulares, laptops y accesorios de las mejores marcas, todo en un solo lugar.</p>
        <button class="hero-button">Explorar Catálogo</button>
      </div>
    </div>

    <!-- Sección de Categorías -->
    <div class="categories">
      <h2 class="section-title">Nuestras Categorías</h2>
      <div class="category-cards">
        <div
            class="category-card"
            v-for="category in categories"
            :key="category.id"
        >
        <img :src="category.image" alt="Categoría" class="category-image" />
        <h3>{{ category.nombre }}</h3>

        </div>
      </div>
    </div>

    <!-- Sección de Promociones -->
    <div class="promotions">
      <h2 class="section-title">Ofertas Especiales</h2>
      <div class="promotion-cards">
        <div
            class="promotion-card"
            v-for="(promotion, index) in promotions"
            :key="index"
        >
          <img :src="promotion.image" alt="Promoción" class="promotion-image" />
          <div class="promotion-info">
            <h4>{{ promotion.title }}</h4>
            <p>{{ promotion.description }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Sección de Marcas -->
    <div class="brands">
      <h2 class="section-title">Trabajamos con las Mejores Marcas</h2>
      <div class="brand-logos">
        <img
            v-for="brand in brands"
            :key="brand.name"
            :src="brand.image"
            alt="Marca"
            class="brand-logo"
        />
      </div>
    </div>

    <!-- Mapa y Contactos -->
    <div class="footer">
      <!-- Mapa -->
      <div class="map-container">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3825.068382076967!2d-68.1145661242216!3d-16.522645041310028!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x915f20ee187a3103%3A0x2f2bb2b7df32a24d!2sUniversidad%20Cat%C3%B3lica%20Boliviana%20%22San%20Pablo%22!5e0!3m2!1ses-419!2sbo!4v1732504180666!5m2!1ses-419!2sbo" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>

      <!-- Contactos -->
      <div class="contact-container">
        <h2 class="section-title">Contáctanos</h2>
        <div class="contact-cards">
          <div class="contact-card" v-for="contact in contacts" :key="contact.name">
            <img src="@/assets/img.png" alt="Contacto" class="contact-image" />
            <div class="contact-info">
              <h4>{{ contact.name }}</h4>
              <p><strong>Teléfono:</strong> {{ contact.phone }}</p>
              <p><strong>Email:</strong> {{ contact.email }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header.vue";
import { CategoriaService } from "../../service/productos/categoriaService";

export default {
  name: 'HomePage',
  components: {HeaderComponent},
  data() {
    return {
      categories: [
  { name: 'Celulares', image: require('@/assets/productos/1celular.png') },
  { name: 'Laptops', image: require('@/assets/productos/1lapto.png') },
  { name: 'Accesorios', image: require('@/assets/productos/1accesorio.png') },
],
      promotions: [
        { title: 'Celulares en Descuento', description: 'Hasta un 30% de descuento.',image: require('@/assets/productos/2cel.jpeg') },
        { title: 'Laptops para Gaming', description: 'Descubre nuestras ofertas en laptops gamer.' ,image: require('@/assets/productos/2lapto.png')},
        { title: 'Accesorios Esenciales', description: 'Audífonos, cargadores y más al mejor precio.',image: require('@/assets/productos/2ac.jpg') },
      ],
      brands: [
        { name: 'Apple',image: require('@/assets/productos/apple.jpeg') },
        { name: 'Samsung',image: require('@/assets/productos/samsung.avif') },
        { name: 'Sony' ,image: require('@/assets/productos/sony.jpg')},
        { name: 'Dell',image: require('@/assets/productos/dell.jpg') },
        { name: 'HP' ,image: require('@/assets/productos/hp.jpg')},
      ],
      contacts: [
        { name: 'Camilo Mendez', phone: '+591 777-12345', email: 'rodrigo.mendez.g@ucb.edu.bo' },
        { name: 'Luis Huanca', phone: '+591 777-54321', email: 'luis.huanca.m@ucb.edu.bo' },
        { name: 'Max Pasten', phone: '+591 777-98765', email: 'max.pasten@ucb.edu.bo' },
        { name: 'Andy Calle', phone: '+591 777-56789', email: 'andy.calle@ucb.edu.bo' },
      ],
    };
  },
  async mounted() {
    await this.fetchCategories();
  },
  methods: {
    async fetchCategories() {
      const categoriesProducts = new CategoriaService()
      try {
        this.categories = await categoriesProducts.listarCategorias();
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Contenedor General */
.home-container {
  font-family: 'Poppins', sans-serif;
  color: #2f3640;
  padding: 20px;
}
.category-image {
  width: 300px;
  height: 250px;
  object-fit: cover;
  margin-bottom: 10px;
}

.promotions-image {
  width: 300px;
  height: 250px;
  object-fit: cover;
  margin-bottom: 10px;
}

.brand-image {
  width: 10px;
  height: 10px;
  object-fit: cover;
  margin-bottom: 0px;
}
/* Banner Principal */
.hero-banner {
  height: 400px;
  background: linear-gradient(
      rgba(0, 0, 0, 0.6),
      rgba(0, 0, 0, 0.6)
  ),
  url('@/assets/img.png') no-repeat center center/cover;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  border-radius: 10px;
  margin-bottom: 40px;
}

.hero-text h1 {
  color: #38d9a9;
  font-size: 3rem;
  text-transform: uppercase;
  margin-bottom: 20px;
}

.hero-text p {
  color: #ffffff;
  font-size: 1.2rem;
  margin-bottom: 30px;
}

.hero-button {
  padding: 10px 20px;
  background-color: #38d9a9;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.hero-button:hover {
  background-color: #20c997;
  transform: scale(1.1);
}

/* Categorías */
.categories {
  text-align: center;
  margin-bottom: 40px;
}

.category-cards {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.category-card {
  background-color: #353b48;
  color: #ffffff;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  width: 250px;
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
}

.category-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

.category-image {
  width: 100%;
  border-radius: 10px;
  margin-bottom: 15px;
}

/* Promociones */
.promotions {
  text-align: center;
  margin-bottom: 40px;
}

.promotion-cards {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.promotion-card {
  background-color: #2f3640;
  color: #ffffff;
  padding: 20px;
  border-radius: 10px;
  width: 300px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.promotion-card:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

.promotion-image {
  width: 100%;
  border-radius: 10px;
  margin-bottom: 15px;
}

.promotion-info h4 {
  font-size: 1.3rem;
  margin-bottom: 10px;
}

.promotion-info p {
  font-size: 1rem;
  color: #dcdde1;
}

/* Marcas */
.brands {
  text-align: center;
}

.brand-logos {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.brand-logo {
  width: 100px;
  height: auto;
  transition: transform 0.3s, filter 0.3s;
  filter: grayscale(100%);
  cursor: pointer;
}

.brand-logo:hover {
  transform: scale(1.1);
  filter: grayscale(0%);
}

/* Títulos */
.section-title {
  font-size: 2rem;
  color: #38d9a9;
  margin-bottom: 20px;
  text-transform: uppercase;
}
/* General */
.home-container {
  font-family: 'Poppins', sans-serif;
  color: #2f3640;
  padding: 20px;
}

/* Footer */
.footer {
  margin-top: 40px;
  padding: 20px;
  background-color: #353b48;
  color: white;
  border-radius: 10px;
}

/* Mapa */
.map-container {
  display: flex;
  margin-bottom: 20px;
  border-radius: 10px;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

/* Contactos */
.contact-container {
  text-align: center;
}

.contact-cards {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}

.contact-card {
  background-color: #2f3640;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  color: white;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  width: 200px;
}

.contact-card:hover {
  transform: translateY(-5px);
  transition: all 0.3s;
}

.contact-image {
  width: 50px;
  height: 50px;
  margin-bottom: 10px;
}

.contact-info h4 {
  font-size: 1.2rem;
  margin-bottom: 10px;
}
</style>
