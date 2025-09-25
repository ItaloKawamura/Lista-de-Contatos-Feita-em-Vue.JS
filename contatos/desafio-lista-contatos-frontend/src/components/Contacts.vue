<template>
  <div id="App">
    <h1>Contatos</h1>
    <ul>
      <li v-for="contato in contatos" :key="contato.email">
        <Contact :contact="contato" />
        <button @click="removeContact(contato)">Remover</button>
      </li>
    </ul>

    <!-- Formulário de Criação de Contato -->
    <div class="contact-form">
      <input v-model="contact.nome" placeholder="Nome" />
      <input v-model="contact.email" placeholder="Email" />
      <input v-model="contact.foto" placeholder="Foto URL" />
      <button @click="createContact">Adicionar Contato</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Contact from './Contact.vue';

export default {
  name: 'App',
  components: { Contact },
  data() {
    return {
      contatos: [],
      contact: { nome: '', email: '', foto: '' },
    };
  },
  mounted() {
    this.getContacts();
  },
  methods: {
    async getContacts() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/contacts');
        this.contatos = response.data.contacts; // ou response.data, depende do backend
      } catch (error) {
        console.error('Erro ao buscar contatos: ', error);
      }
    },

    async createContact() {
      try {
        await axios.post('http://127.0.0.1:5000/contacts', {
          nome: this.contact.nome,
          email: this.contact.email,
          foto: this.contact.foto
        });
        // Atualiza a lista de contatos imediatamente após adicionar um contato
        await this.getContacts();
        this.contact = { nome: '', email: '', foto: '' };
      } catch (error) {
        console.error('Erro ao adicionar contato:', error);
      }
    },

    async removeContact(contact) {
      if (confirm(`Apagar o contato: ${contact.email}?`)) {
        try {
          await axios.delete(`http://127.0.0.1:5000/contacts/${contact.email}`);
          this.contatos.splice(this.contatos.indexOf(contact), 1);
        } catch (error) {
          console.error('Erro ao remover o contato', error);
        }
      }
    },
  }
};
</script>  

<style scoped>
#App {
  font-family: Avenir, Helvetica, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px;
  margin: 10px;
  border: 1px solid #000000; /* Borda verde adicionada */
  border-radius: 5px;
  transition: all 0.3s ease;
}

li:hover {
  background-color: #ffffe1;
  transform: scale(1.02);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}

button {
  background-color: #d90808; /* Alterado para uma cor laranja */
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  border: 2px solid #d90808; /* Borda do botão */
}

button:hover {
  background-color: #e64a19;
}

button:active {
  background-color: #d32f2f;
}

button:focus {
  outline: none;
}

.contact-form {
  margin-top: 20px;
}

.contact-form input {
  padding: 10px;
  margin: 5px;
  width: 250px;
  border-radius: 5px;
}

.contact-form button {
  background-color: #4caf50;
  color: white;
  padding: 10px;
  margin-top: 10px;
  border: none;
  border-radius: 5px;
}

.contact-form button:hover {
  background-color: #45a049;
}
</style>
