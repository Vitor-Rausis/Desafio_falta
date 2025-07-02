<template>
  <div class="cep-form">
    <h1>Consulta de CEP</h1>
    <form @submit.prevent="fetchCep">
      <div class="form-group">
        <label for="cep">Digite o CEP:</label>
        <input
          id="cep"
          v-model="cep"
          type="text"
          placeholder="00000-000 ou 00000000"
          @input="formatCep"
        />
        <button type="submit">Consultar</button>
      </div>
    </form>

    <div v-if="loading" class="loading">Carregando...</div>
    <div v-if="error" class="error">{{ error }}</div>

    <div v-if="cepData" class="result">
      <h2>Resultado:</h2>
      <p><strong>CEP:</strong> {{ cepData.cep }}</p>
      <p><strong>Logradouro:</strong> {{ cepData.logradouro || 'Não informado' }}</p>
      <p><strong>Complemento:</strong> {{ cepData.complemento || 'Não informado' }}</p>
      <p><strong>Bairro:</strong> {{ cepData.bairro || 'Não informado' }}</p>
      <p><strong>Cidade:</strong> {{ cepData.localidade }}</p>
      <p><strong>Estado:</strong> {{ cepData.uf }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cep: '',
      cepData: null,
      loading: false,
      error: null
    }
  },
  methods: {
    formatCep() {
      // Remove caracteres não numéricos
      let cleaned = this.cep.replace(/\D/g, '')
      
      // Formata como 00000-000 se tiver mais de 5 dígitos
      if (cleaned.length > 5) {
        cleaned = cleaned.substring(0, 5) + '-' + cleaned.substring(5, 8)
      }
      
      this.cep = cleaned
    },
    async fetchCep() {
      if (!this.cep) {
        this.error = 'Por favor, digite um CEP'
        return
      }

      this.loading = true
      this.error = null
      this.cepData = null

      try {
        const cleanedCep = this.cep.replace(/\D/g, '')
        const response = await fetch(`http://localhost:8000/cep/${cleanedCep}`)
        
        if (!response.ok) {
          const errorData = await response.json()
          throw new Error(errorData.detail || 'Erro ao consultar CEP')
        }

        this.cepData = await response.json()
      } catch (err) {
        this.error = err.message
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.cep-form {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.form-group {
  margin-bottom: 20px;
}

input {
  padding: 8px;
  width: 150px;
  margin-right: 10px;
}

button {
  padding: 8px 16px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #369f6e;
}

.loading, .error {
  margin: 20px 0;
  padding: 10px;
  border-radius: 4px;
}

.loading {
  background-color: #f8f8f8;
  color: #555;
}

.error {
  background-color: #ffebee;
  color: #f44336;
}

.result {
  margin-top: 20px;
  padding: 15px;
  background-color: #f5f5f5;
  border-radius: 4px;
}

.result p {
  margin: 5px 0;
}
</style>