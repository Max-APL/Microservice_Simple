<template>
  <div>
    <HeaderComponent />
    <h2 class="heading">Ventas</h2>
    <div class="container">
      <button class="create-button" @click="redirectToCreateSale">Crear Venta</button>
      <div v-if="loading" class="loading">Cargando ventas...</div>
      <div v-else>
        <table class="sales-table">
          <thead>
          <tr>
            <th>ID Venta</th>
            <th>Cliente</th>
            <th>Fecha</th>
            <th>Total</th>
            <th>Acciones</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="venta in ventas" :key="venta.id_venta">
            <td>{{ venta.id_venta }}</td>
            <td>{{ venta.cliente }}</td>
            <td>{{ venta.fecha }}</td>
            <td>${{ venta.total }}</td>
            <td>
              <button @click="viewSaleDetails(venta)" class="action-button">Ver más</button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Modal para ver detalles de una venta -->
    <div v-if="showDetailsModal" class="modal">
      <div class="modal-content">
        <h3>Detalles de la Venta</h3>
        <table class="details-table">
          <thead>
          <tr>
            <th>Producto</th>
            <th>Cantidad</th>
            <th>Subtotal</th>
            <th>Acciones</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="detalle in detallesVenta" :key="detalle.id">
            <td>{{ detalle.nombre_producto }}</td>
            <td>{{ detalle.cantidad }}</td>
            <td>${{ detalle.subtotal }}</td>
            <td>
              <button @click="openEditDetailModal(detalle)" class="action-button">Editar</button>
              <button @click="deleteDetail(detalle.id)" class="action-button delete-button">Eliminar</button>
            </td>
          </tr>
          </tbody>
        </table>
        <div class="modal-actions">
          <button @click="closeDetailsModal" class="modal-button">Cerrar</button>
        </div>
      </div>
    </div>

    <!-- Modal para editar detalle de venta -->
    <div v-if="showEditDetailModal" class="modal">
      <div class="modal-content">
        <h3>Editar Detalle de Venta</h3>
        <form @submit.prevent="updateDetail">
          <label for="producto">Producto:</label>
          <select id="producto" v-model="detalleForm.id_producto" required>
            <option
                v-for="producto in productos"
                :key="producto.id_producto"
                :value="producto.id_producto"
            >
              {{ producto.nombre }}
            </option>
          </select>

          <label for="cantidad">Cantidad:</label>
          <input
              id="cantidad"
              v-model="detalleForm.cantidad"
              type="number"
              min="1"
              required
          />

          <div class="modal-actions">
            <button type="submit" class="modal-button">Guardar</button>
            <button type="button" @click="closeEditDetailModal" class="modal-button cancel-button">
              Cancelar
            </button>
          </div>
        </form>
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
      ventas: [],
      detallesVenta: [],
      productos: [],
      detalleForm: { id_producto: '', cantidad: '' },
      selectedDetalle: null,
      loading: true,
      showDetailsModal: false,
      showEditDetailModal: false,
    };
  },
  methods: {
    async fetchVentas() {
      const ventaService = new VentaService();
      try {
        this.ventas = await ventaService.listarVentas();
      } catch (error) {
        console.error('Error al obtener las ventas:', error);
      } finally {
        this.loading = false;
      }
    },
    async fetchProductos() {
      const productoService = new ProductoService();
      try {
        this.productos = await productoService.listarProductos();
      } catch (error) {
        console.error('Error al obtener los productos:', error);
      }
    },
    async viewSaleDetails(venta) {
      const detalleVentaService = new DetalleVentaService();
      try {
        this.detallesVenta = await detalleVentaService.listarDetallesPorVenta(
            venta.id_venta
        );
        this.showDetailsModal = true;
      } catch (error) {
        console.error('Error al obtener los detalles de la venta:', error);
      }
    },
    closeDetailsModal() {
      this.showDetailsModal = false;
    },
    async deleteDetail(id) {
      const detalleVentaService = new DetalleVentaService();
      try {
        await detalleVentaService.eliminarDetalleVenta(id);
        this.detallesVenta = this.detallesVenta.filter(
            (detalle) => detalle.id !== id
        );
      } catch (error) {
        console.error('Error al eliminar el detalle:', error);
      }
    },
    openEditDetailModal(detalle) {
      this.selectedDetalle = detalle;
      this.detalleForm = {
        id_producto: detalle.id_producto,
        cantidad: detalle.cantidad,
      };
      this.showEditDetailModal = true;
    },
    closeEditDetailModal() {
      this.showEditDetailModal = false;
    },
    async updateDetail() {
      const detalleVentaService = new DetalleVentaService();
      try {
        await detalleVentaService.actualizarDetalleVenta(
            this.selectedDetalle.id,
            this.detalleForm
        );
        const index = this.detallesVenta.findIndex(
            (detalle) => detalle.id === this.selectedDetalle.id
        );
        if (index !== -1) {
          this.detallesVenta[index] = {
            ...this.selectedDetalle,
            ...this.detalleForm,
            subtotal:
                this.detalleForm.cantidad *
                this.productos.find(
                    (p) => p.id_producto === this.detalleForm.id_producto
                ).precio_unitario,
          };
        }
        this.closeEditDetailModal();
      } catch (error) {
        console.error('Error al actualizar el detalle:', error);
      }
    },
    redirectToCreateSale() {
      this.$router.push('/crear_venta');
    },
  },
  async mounted() {
    await Promise.all([this.fetchVentas(), this.fetchProductos()]);
  },
};
</script>

<style scoped>
/* Encabezado */
.heading {
  font-family: 'Poppins', sans-serif;
  font-size: 2rem;
  font-weight: 600;
  color: #38d9a9;
  text-align: center;
  margin: 20px 0;
  text-transform: uppercase;
}

/* Contenedor principal */
.container {
  margin: 20px auto;
  max-width: 1200px;
}

/* Botón Crear Venta */
.create-button {
  background-color: #38d9a9;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-bottom: 20px;
  display: inline-block;
  float: right; /* Alineado a la derecha */
}

.create-button:hover {
  background-color: #20c997;
}

/* Tabla de Ventas */
.sales-table {
  width: 100%;
  border-collapse: collapse;
  margin: 0 auto;
  background-color: #2f3640;
  color: #fff;
  text-align: left;
  border-radius: 5px; /* Bordes redondeados */
  overflow: hidden; /* Mantener el diseño limpio */
  padding: 15px; /* Espacio adicional dentro del contenedor */
}

.sales-table th,
.sales-table td {
  padding: 10px 15px;
  border-bottom: 1px solid #444;
}

.sales-table th {
  background-color: #353b48;
  font-weight: bold;
}

.sales-table tr:hover {
  background-color: #3b4048;
}

/* Botones de acción */
.action-button {
  background-color: #38d9a9;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.action-button:hover {
  background-color: #20c997;
}

.delete-button {
  background-color: #e74c3c;
}

.delete-button:hover {
  background-color: #c0392b;
}

/* Modal */
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
  max-width: 500px;
  text-align: center;
}

.modal-content h3 {
  color: #38d9a9;
  margin-bottom: 20px;
}

.details-table {
  width: 100%;
  border-collapse: collapse;
  margin: 0 auto;
  background-color: #2f3640;
  color: #fff;
}

.details-table th,
.details-table td {
  padding: 10px 15px;
  border-bottom: 1px solid #444;
}

.details-table th {
  background-color: #353b48;
  font-weight: bold;
}

.modal-actions {
  margin-top: 20px;
  text-align: right;
}

.modal-button {
  background-color: #38d9a9;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.modal-button:hover {
  background-color: #20c997;
}
</style>

