<template>
  <div>
    <HeaderComponent />
    <h2 class="heading">Productos</h2>
    <button class="create-button" @click="openCreateModal">Crear Producto</button>
    <div v-if="loading" class="loading">Cargando productos...</div>
    <div v-else class="product-list">
      <article v-for="product in products" :key="product.id_producto" class="article-wrapper">
        <div class="rounded-lg container-project">
          <img
              :src="product.image || defaultImage"
              alt="Producto"
              class="product-image"
          />
        </div>
        <div class="project-info">
          <div class="flex-pr">
            <div class="project-title text-nowrap">{{ product.nombre }}</div>
          </div>
          <p class="product-price">${{ product.precio }}</p>
          <p class="product-description">{{ product.descripcion }}</p>
          <div class="actions">
            <button @click="openDetailModal(product)" class="action-button">Ver Detalle</button>
            <button @click="openEditModal(product)" class="action-button">Editar</button>
            <button @click="openDeleteModal(product)" class="action-button delete-button">Eliminar</button>
          </div>
        </div>
      </article>
    </div>

    <!-- Modal para crear producto -->
    <div v-if="showCreateModal" class="modal">
      <div class="modal-content">
        <h3>Crear Producto</h3>
        <form @submit.prevent="createProduct">
          <label for="nombre">Nombre:</label>
          <input id="nombre" v-model="form.nombre" type="text" placeholder="Nombre" required style="max-width: 380px"/>

          <label for="precio">Precio:</label>
          <input id="precio" v-model="form.precio" type="number" step="0.01" placeholder="Precio" required style="max-width: 380px"/>

          <label for="descripcion">Descripción:</label>
          <textarea id="descripcion" v-model="form.descripcion" placeholder="Descripción" style="max-width: 380px"></textarea>

          <label for="categoria">Categoría:</label>
          <select id="categoria" v-model="form.id_categoria" required>
            <option v-for="categoria in categorias" :key="categoria.id_categoria" :value="categoria.id_categoria">
              {{ categoria.nombre }}
            </option>
          </select>

          <label for="marca">Marca:</label>
          <select id="marca" v-model="form.id_marca" required>
            <option v-for="marca in marcas" :key="marca.id_marca" :value="marca.id_marca">
              {{ marca.nombre }}
            </option>
          </select>

          <div class="modal-actions">
            <button type="submit" class="modal-button">Guardar</button>
            <button type="button" @click="closeCreateModal" class="modal-button cancel-button">Cancelar</button>
          </div>
        </form>

      </div>
    </div>

    <!-- Modal para editar producto -->
    <div v-if="showEditModal" class="modal">
      <div class="modal-content">
        <h3>Editar Producto</h3>
        <form @submit.prevent="updateProduct">
          <label for="edit-nombre">Nombre:</label>
          <input
              id="edit-nombre"
              v-model="form.nombre"
              type="text"
              placeholder="Nombre"
              required
          />

          <label for="edit-precio">Precio:</label>
          <input
              id="edit-precio"
              v-model="form.precio"
              type="number"
              step="0.01"
              placeholder="Precio"
              required
          />

          <label for="edit-descripcion">Descripción:</label>
          <textarea
              id="edit-descripcion"
              v-model="form.descripcion"
              placeholder="Descripción"
          ></textarea>

          <label for="edit-categoria">Categoría:</label>
          <select id="edit-categoria" v-model="form.id_categoria" required>
            <option
                v-for="categoria in categorias"
                :key="categoria.id_categoria"
                :value="categoria.id_categoria"
            >
              {{ categoria.nombre }}
            </option>
          </select>

          <label for="edit-marca">Marca:</label>
          <select id="edit-marca" v-model="form.id_marca" required>
            <option v-for="marca in marcas" :key="marca.id_marca" :value="marca.id_marca">
              {{ marca.nombre }}
            </option>
          </select>

          <div class="modal-actions">
            <button type="submit" class="modal-button">Guardar</button>
            <button type="button" @click="closeEditModal" class="modal-button cancel-button">
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Modal para ver detalle -->
    <div v-if="showDetailModal" class="modal">
      <div class="modal-content">
        <h3>Detalle del Producto</h3>
        <p><strong>Nombre:</strong> {{ selectedProduct.nombre }}</p>
        <p><strong>Precio:</strong> ${{ selectedProduct.precio }}</p>
        <p><strong>Descripción:</strong> {{ selectedProduct.descripcion }}</p>
        <p><strong>Categoría:</strong> {{ selectedProduct.categoria }}</p>
        <p><strong>Marca:</strong> {{ selectedProduct.marca }}</p>
        <div class="modal-actions">
          <button type="button" @click="closeDetailModal" class="modal-button">Cerrar</button>
        </div>
      </div>
    </div>

    <!-- Modal para confirmar eliminación -->
    <div v-if="showDeleteModal" class="modal">
      <div class="modal-content">
        <h3>Eliminar Producto</h3>
        <p>¿Está seguro de que desea eliminar el producto "{{ selectedProduct.nombre }}"?</p>
        <div class="modal-actions">
          <button @click="deleteProduct" class="modal-button delete-button">Sí, eliminar</button>
          <button @click="closeDeleteModal" class="modal-button cancel-button">Cancelar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ProductoService} from "../../service/productos/productoService";
import { CategoriaService} from "../../service/productos/categoriaService";
import { MarcaService} from "../../service/productos/marcaService";
import HeaderComponent from "@/components/Header.vue";

export default {
  name: 'ProductList',
  components: {HeaderComponent},
  data() {
    return {
      defaultImage: 'https://cdn-icons-png.flaticon.com/512/2649/2649150.png',
      products: [],
      categorias: [],
      marcas: [],
      loading: true,
      form: {nombre: '', precio: '', descripcion: '', id_categoria: '', id_marca: ''},
      selectedProduct: null,
      showCreateModal: false,
      showEditModal: false,
      showDetailModal: false,
      showDeleteModal: false,
    };
  },
  methods: {
    async fetchProducts() {
      const productoService = new ProductoService();
      try {
        this.products = await productoService.listarProductos();
      } catch (error) {
        console.error('Error al obtener los productos:', error);
      } finally {
        this.loading = false;
      }
    },
    async fetchCategorias() {
      const categoriaService = new CategoriaService();
      try {
        this.categorias = await categoriaService.listarCategorias();
      } catch (error) {
        console.error('Error al obtener las categorías:', error);
      }
    },
    async fetchMarcas() {
      const marcaService = new MarcaService();
      try {
        this.marcas = await marcaService.listarMarcas();
      } catch (error) {
        console.error('Error al obtener las marcas:', error);
      }
    },
    openCreateModal() {
      this.showCreateModal = true;
    },
    closeCreateModal() {
      this.showCreateModal = false;
    },
    async createProduct() {
      const productoService = new ProductoService();
      try {
        await productoService.agregarProducto(this.form);
        this.fetchProducts();
      } catch (error) {
        console.error('Error al crear el producto:', error);
      } finally {
        this.closeCreateModal();
      }
    },
    openEditModal(product) {
      this.selectedProduct = {...product};
      this.form = {...product};
      this.showEditModal = true;
    },
    closeEditModal() {
      this.showEditModal = false;
    },
    async updateProduct() {
      const productoService = new ProductoService();
      try {
        await productoService.modificarProducto(this.selectedProduct.id_producto, this.form);
        this.fetchProducts();
      } catch (error) {
        console.error('Error al actualizar el producto:', error);
      } finally {
        this.closeEditModal();
      }
    },
    openDetailModal(product) {
      this.selectedProduct = {...product};
      this.showDetailModal = true;
    },
    closeDetailModal() {
      this.showDetailModal = false;
    },
    openDeleteModal(product) {
      this.selectedProduct = {...product};
      this.showDeleteModal = true;
    },
    closeDeleteModal() {
      this.showDeleteModal = false;
    },
    async deleteProduct() {
      const productoService = new ProductoService();
      try {
        await productoService.borrarProducto(this.selectedProduct.id_producto);
        this.fetchProducts();
      } catch (error) {
        console.error('Error al eliminar el producto:', error);
      } finally {
        this.closeDeleteModal();
      }
    },
  },
  async mounted() {
    await Promise.all([this.fetchProducts(), this.fetchCategorias(), this.fetchMarcas()]);
  },
};
</script>

<style scoped>
/* Fondo general */
body {
  background-color: #1e272e; /* Gris oscuro */
  margin: 0;
  padding: 0;
}

/* Encabezado */
.heading {
  font-family: 'Poppins', sans-serif;
  font-size: 3rem;
  font-weight: 600;
  color: #38d9a9; /* Turquesa */
  text-align: center;
  margin: 20px 0;
  text-transform: uppercase;
  letter-spacing: 2px;
  animation: fadeIn 1.2s ease-out;
}

/* Lista de productos */
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin: 20px auto;
  max-width: 1200px;
  padding: 20px;
}

/* Tarjetas de productos */
.article-wrapper {
  background-color: #2f3640; /* Gris oscuro */
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.article-wrapper:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
}

/* Contenedor de imágenes */
.container-project {
  height: 200px;
  background-color: #353b48; /* Gris intermedio */
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.product-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}

.article-wrapper:hover .product-image {
  transform: scale(1.1);
}

/* Información del producto */
.project-info {
  padding: 15px;
}

.project-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: #ffffff;
  margin: 0;
}

.project-hover {
  background-color: #38d9a9; /* Turquesa */
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.project-hover:hover {
  background-color: #20c997; /* Verde oscuro */
  transform: rotate(-15deg);
}

/* Precio */
.product-price {
  font-size: 1.2rem;
  color: #44bd32; /* Verde */
  font-weight: bold;
  margin-top: 10px;
}

/* Descripción */
.product-description {
  font-size: 0.9rem;
  color: #dcdde1; /* Gris claro */
  margin: 10px 0;
}

/* Categoría */
.project-type {
  background-color: #38d9a9; /* Turquesa */
  color: white;
  padding: 5px 10px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: bold;
  text-transform: uppercase;
}

/* Animaciones */
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(-20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
/* Se mantienen estilos originales y se agregan estilos personalizados para los modales y botones */
.action-button {
  background-color: #38d9a9;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
  margin: 5px;
}

.delete-button {
  background-color: #e74c3c;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: #2f3640;
  padding: 20px;
  border-radius: 10px;
  width: 90%;
  max-width: 400px;
  text-align: left; /* Alineación izquierda */
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.modal-content h3 {
  color: #38d9a9;
  margin-bottom: 20px;
  font-size: 1.5rem;
  text-align: center; /* Centrado del encabezado */
}

.modal-content form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.modal-content form label {
  font-size: 0.9rem;
  color: #dcdde1;
  margin-bottom: 5px;
}

.modal-content form input,
.modal-content form textarea,
.modal-content form select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ced4da;
  border-radius: 5px;
  font-size: 1rem;
  background-color: #353b48;
  color: #fff;
}

.modal-content form textarea {
  resize: none;
  height: 80px;
}

.modal-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.modal-button {
  background-color: #38d9a9;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.modal-button:hover {
  background-color: #20c997;
}

.cancel-button {
  background-color: #7f8c8d;
}

.delete-button:hover {
  background-color: #c0392b;
}


</style>
