<template>
  <HeaderComponent />
  <div class="venta-container">
    <h1 class="screen-title">Registrar Venta</h1>

    <div class="columns">
      <!-- Columna de Productos Disponibles -->
      <div class="product-list">
        <h2 class="section-title">Productos Disponibles</h2>
        <div class="search-bar">
          <input
              v-model="searchQuery"
              placeholder="Buscar producto..."
              class="input-search"
          />
          <button @click="searchProduct" class="btn-search">🔍</button>
        </div>
        <div class="product-panel">
          <div
              v-for="product in filteredProducts"
              :key="product.id_producto"
              class="product-item"
          >
            <div class="product-info">
              <h4>{{ product.nombre }}</h4>
              <p>{{ product.descripcion }}</p>
              <div class="product-details">
                <span><strong>Precio:</strong> ${{ product.precio }}</span>
              </div>
            </div>
            <button class="btn-add" @click="addProductToSale(product)">+</button>
          </div>
        </div>
      </div>

      <!-- Columna de Formulario -->
      <div class="venta-form">
        <h2 class="section-title">Registrar Detalles de Venta</h2>
        <form @submit.prevent="submitSale" class="form-layout">
          <div class="form-group">
            <label for="cliente">Cliente</label>
            <select
                v-model="newSale.id_cliente"
                id="cliente"
                required
                class="input-select"
            >
              <option
                  v-for="cliente in clientes"
                  :key="cliente.id_cliente"
                  :value="cliente.id_cliente"
              >
                {{ cliente.nombre }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label for="fecha">Fecha</label>
            <input
                v-model="newSale.fecha"
                id="fecha"
                type="date"
                required
                class="input-text"
                style="max-width: 570px"
            />
          </div>

          <div class="form-group total-display">
            <strong>Total:</strong>
            <span>${{ totalCost }}</span>
          </div>

          <button type="submit" class="btn-submit">Registrar Venta</button>
        </form>

        <h3 class="section-title">Productos Seleccionados</h3>
        <table class="venta-table">
          <thead>
          <tr>
            <th>Nombre</th>
            <th>Cantidad</th>
            <th>Precio</th>
            <th>Subtotal</th>
            <th>Acción</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(product, index) in saleProducts" :key="index">
            <td>{{ product.nombre }}</td>
            <td>
              <input
                  v-model.number="product.cantidad"
                  type="number"
                  placeholder="Cantidad"
                  required
                  class="input-quantity"
              />
            </td>
            <td>${{ product.precio }}</td>
            <td>${{ (product.cantidad * product.precio).toFixed(2) }}</td>
            <td>
              <button
                  @click="removeProductFromSale(index)"
                  class="btn-delete"
              >
                🗑️
              </button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>



<script>
import { VentaService} from "../../service/ventas/ventaService";
import { DetalleVentaService} from "../../service/ventas/detalleVentaService";
import { ProductoService} from "../../service/productos/productoService";
import HeaderComponent from "@/components/Header.vue";

export default {
  components: {HeaderComponent},
  data() {
    return {
      searchQuery: '',
      products: [],
      saleProducts: [],
      clientes: [
        { id_cliente: 1, nombre: 'Juan Pérez' },
        { id_cliente: 2, nombre: 'María López' },
        { id_cliente: 3, nombre: 'Carlos Gómez' },
      ],
      newSale: {
        id_cliente: '',
        fecha: '',
      },
    };
  },
  computed: {
    filteredProducts() {
      return this.products.filter((product) =>
          product.nombre.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
    totalCost() {
      // Redondea el total a 2 decimales
      return parseFloat(
          this.saleProducts.reduce(
              (sum, product) => sum + product.cantidad * product.precio,
              0
          ).toFixed(2)
      );
    },
  },
  methods: {
    async loadProducts() {
      const productoService = new ProductoService();
      try {
        this.products = await productoService.listarProductos();
      } catch (error) {
        console.error('Error al cargar productos:', error);
      }
    },
    searchProduct() {
      console.log('Buscando producto:', this.searchQuery);
    },
    addProductToSale(product) {
      const exists = this.saleProducts.find(
          (item) => item.id_producto === product.id_producto
      );
      if (!exists) {
        this.saleProducts.push({ ...product, cantidad: 1 });
      } else {
        alert('El producto ya está en la lista de venta');
      }
    },
    removeProductFromSale(index) {
      this.saleProducts.splice(index, 1);
    },
    async submitSale() {
      try {
        // Crear la venta
        const ventaService = new VentaService();
        const ventaData = {
          id_cliente: this.newSale.id_cliente,
          fecha: this.newSale.fecha,
          total: parseFloat(this.totalCost.toFixed(2)), // Redondear total a 2 decimales
        };

        // Validar campos obligatorios de la venta
        if (!ventaData.id_cliente || !ventaData.fecha || ventaData.total <= 0) {
          throw new Error('Faltan datos obligatorios para la venta');
        }

        const idVenta = await ventaService.agregarVenta(ventaData);

        // Crear los detalles de la venta
        const detalleVentaService = new DetalleVentaService();
        for (const product of this.saleProducts) {
          const detalleData = {
            id_venta: idVenta.id_venta, // ID de la venta creada
            id_producto: product.id_producto, // ID del producto
            cantidad: product.cantidad, // Cantidad seleccionada
          };

          // Validar detalle de venta antes de enviarlo
          if (!detalleData.id_producto || detalleData.cantidad <= 0) {
            console.error('Detalle inválido:', detalleData);
            throw new Error('Faltan datos en un detalle de venta');
          }

          // Enviar detalle al backend
          await detalleVentaService.agregarDetalleVenta(detalleData);
        }

        alert('Venta registrada con éxito');
        this.saleProducts = [];
        this.newSale = { id_cliente: '', fecha: '' };
      } catch (error) {
        console.error('Error al registrar la venta o detalle:', error);
        alert('Ocurrió un error al registrar la venta. Verifica los datos.');
      }
    },
  },
  async mounted() {
    await this.loadProducts();
  },
};
</script>


<style scoped>
.venta-container {
  margin: 20px auto;
  max-width: 1200px;
  padding: 20px;
}

.columns {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}

/* Columna de productos */
.product-list {
  width: 45%;
  background-color: #2f3640;
  border-radius: 10px;
  padding: 15px;
  overflow-y: auto;
  height: 700px;
  max-height: 1000px; /* Limitar altura con scroll */
}

.product-panel {
  margin-top: 15px;
  max-height: 800px;
  overflow-y: auto;
}

.product-item {
  background-color: #353b48;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.product-info h4 {
  font-size: 1.1rem;
  color: #ffffff;
}

.product-info p {
  font-size: 0.9rem;
  color: #dcdde1;
}

.product-details {
  font-size: 0.9rem;
  margin-top: 10px;
}

.btn-add {
  background-color: #38d9a9;
  border: none;
  color: white;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
}

.btn-add:hover {
  background-color: #20c997;
}

/* Columna de formulario */
.venta-form {
  width: 50%;
  background-color: #2f3640;
  border-radius: 10px;
  padding: 15px;
}

.form-layout .form-group {
  margin-bottom: 15px;
}

.input-select,
.input-text {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ced4da;
  border-radius: 5px;
}

.total-display {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1.2rem;
  color: #38d9a9;
  margin-top: 15px;
  padding: 10px;
  background-color: #353b48;
  border-radius: 5px;
}

/* Tabla de productos seleccionados */
.venta-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  background-color: #353b48;
  border-radius: 10px;
  overflow: hidden;
}

.venta-table th,
.venta-table td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #444;
}

.venta-table th {
  background-color: #444b55;
  color: #ffffff;
}

.venta-table tbody tr:hover {
  background-color: #3b4048;
}

.btn-delete {
  background-color: #e74c3c;
  border: none;
  color: white;
  border-radius: 5px;
  padding: 5px;
  cursor: pointer;
}

.btn-delete:hover {
  background-color: #c0392b;
}

/* Encabezados */
.section-title {
  font-size: 1.4rem;
  color: #38d9a9;
  margin-bottom: 15px;
}
</style>
