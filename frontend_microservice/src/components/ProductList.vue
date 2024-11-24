<template>
  <div>
    <h2 class="heading">Productos</h2>
    <div class="product-list">
      <article v-for="product in products" :key="product.id" class="article-wrapper">
        <div class="rounded-lg container-project">
          <img
            :src="product.image || defaultImage"
            alt="Producto"
            class="product-image"
          />
        </div>
        <div class="project-info">
          <div class="flex-pr">
            <div class="project-title text-nowrap">{{ product.name }}</div>
            <div class="project-hover">
              <!-- Ícono de compra (carrito) -->
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="3em"
                height="3em"
                viewBox="0 0 24 24"
                stroke-width="2"
                fill="none"
                stroke="currentColor"
              >
                <path
                  d="M7 4V2h10v2h3l3 12H4L7 4z"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                ></path>
                <circle cx="10" cy="19" r="2" fill="currentColor"></circle>
                <circle cx="18" cy="19" r="2" fill="currentColor"></circle>
              </svg>
            </div>
          </div>
          <p class="product-price">${{ product.price }}</p>
          <p class="product-description">{{ product.description }}</p>
          <div class="types">
            <span class="project-type">{{ product.category }}</span>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductList',
  data() {
    return {
      defaultImage: 'https://cdn-icons-png.flaticon.com/512/2649/2649150.png',
      products: [
        {
          id: 1,
          name: 'Producto 1',
          price: 100,
          description: 'Descripción breve del Producto 1',
          category: 'Electrónica',
          image: '', // Deja vacío para usar imagen predeterminada si no hay URL
        },
        {
          id: 2,
          name: 'Producto 2',
          price: 150,
          description: 'Descripción breve del Producto 2',
          category: 'Hogar',
          image: '',
        },
        {
          id: 3,
          name: 'Producto 3',
          price: 200,
          description: 'Descripción breve del Producto 3',
          category: 'Moda',
          image: '',
        },
        {
          id: 4,
          name: 'Producto 4',
          price: 120,
          description: 'Descripción breve del Producto 4',
          category: 'Electrónica',
          image: '',
        },
        {
          id: 5,
          name: 'Producto 5',
          price: 170,
          description: 'Descripción breve del Producto 5',
          category: 'Hogar',
          image: '',
        },
        {
          id: 6,
          name: 'Producto 6',
          price: 210,
          description: 'Descripción breve del Producto 6',
          category: 'Moda',
          image: '',
        },
      ],
    };
  },
};
</script>

<style scoped>
/* Diseño profesional y atractivo para la lista de productos */
body {
  background-color: #4444bd; /* Fondo atractivo */
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  margin: 0;
  padding: 0;
}

.heading {
  background-color: rgb(238, 195, 142);
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 30px;
  text-align: center;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* Sombra para el título */

}

.product-list {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px; /* Aumenta el espacio entre las tarjetas en ambas direcciones */
  margin: 0 auto;
  max-width: 1200px;
  padding: 20px;
  background-color: #333;
  border-radius: 15px;
  
}

.article-wrapper {
  border-radius: 15px;
  padding: 15px;
  background-color: #f5f5f5;
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease-in-out;
  cursor: pointer;
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-left: 30px; /* Margen horizontal */
  margin-right: 30px; /* Margen horizontal */
  margin-bottom: 25px; /* Margen inferior para aumentar la separación vertical */
}


.article-wrapper:hover {
  transform: translateY(-15px);
  box-shadow: 0 20px 30px rgba(0, 0, 0, 0.2);
}

.article-wrapper:active {
  transform: translateY(0);
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
}

.container-project {
  width: 100%;
  height: 200px;
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  overflow: hidden;
}

.product-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease-in-out;
}

.article-wrapper:hover .product-image {
  transform: scale(1.1);
}

.project-info {
  padding: 10px;
}

.flex-pr {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.project-title {
  font-size: 1.8rem;
  font-weight: bold;
  color: #333;
  margin: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.project-hover {
  border-radius: 50%;
  width: 45px;
  height: 45px;
  padding: 10px;
  background-color: #ddd;
  transition: all 0.3s ease;
}

.project-hover:hover {
  background-color: #4e84ff;
}

.product-price {
  font-size: 1.4rem;
  color: #27ae60;
  margin: 10px 0;
}

.product-description {
  font-size: 1rem;
  color: #7f8c8d;
  margin-bottom: 15px;
}

.types {
  display: flex;
  gap: 10px;
}

.project-type {
  background-color: #3498db;
  color: white;
  padding: 5px 10px;
  border-radius: 15px;
  font-size: 12px;
  font-weight: bold;
}

/* From Uiverse.io by Amine-maker */
.article-wrapper {
  -webkit-transition: 0.15s all ease-in-out;
  transition: 0.15s all ease-in-out;
  border-radius: 10px;
  padding: 5px;
  border: 4px solid transparent;
  background-color: rgb(85, 238, 167);
}

.article-wrapper:hover {
  -webkit-box-shadow: 10px 10px 0 #4e84ff, 20px 20px 0 #4444bd;
  box-shadow: 10px 10px 0 #4e84ff, 20px 20px 0 #4444bd;
  border-color: #0578c5;
  -webkit-transform: translate(-20px, -20px);
  -ms-transform: translate(-20px, -20px);
  transform: translate(-20px, -20px);
}

.article-wrapper:active {
  -webkit-box-shadow: none;
  box-shadow: none;
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  transform: translate(0, 0);
}

.project-hover {
  width: 50px;
  height: 50px;
  padding: 9px;
  -webkit-transition: all 0.3s ease;
  transition: all 0.3s ease;
}

.article-wrapper:hover .project-hover {
  -webkit-transform: rotate(-45deg);
  -ms-transform: rotate(-45deg);
  transform: rotate(-45deg);
  background-color: #a6c2f0;
}
/* Agregamos fuente desde Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

.heading {
  font-family: 'Poppins', sans-serif; /* Usando la fuente Poppins */
  font-size: 4rem; /* Tamaño grande para un efecto impactante */
  font-weight: 700; /* Negrita */
  color: #3a3a3a; /* Color de texto elegante */
  text-transform: uppercase; /* Convertir a mayúsculas */
  text-align: center;
  position: relative;
  letter-spacing: 5px; /* Espaciado de letras */
  margin-top: 50px;
  margin-bottom: 30px;
  animation: fadeIn 1.5s ease-out, slideIn 1s ease-out;
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Sombra sutil */
}

/* Animación de aparición */
@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

/* Animación de deslizamiento */
@keyframes slideIn {
  0% {
    transform: translateY(-20px);
  }
  100% {
    transform: translateY(0);
  }
}

/* Hover effect */
.heading:hover {
  color: #007CFF; /* Cambio de color en hover */
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.4); /* Sombra más intensa en hover */
  transform: translateY(-5px); /* Deslizamiento hacia arriba */
  transition: all 0.3s ease; /* Transición suave */
}
</style>
