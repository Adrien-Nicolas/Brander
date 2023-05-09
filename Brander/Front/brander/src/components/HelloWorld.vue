<template>
  <div id="brand_generator">
    <div class="container-fluid bg-transparent text-light py-5">

      <div class="text-center mb-5">
        <h1 class="display-3">Brand generator</h1>
      </div>

      <div class="row justify-content-center">
        <div class="col-lg-6">

          <form @submit.prevent="generateDesign">
            <div class="mb-3">
              <label for="project-description" class="form-label">Project Description:</label>
              <textarea id="project-description" class="form-control" v-model="projectDescription" rows="5"></textarea>
            </div>
            <div class="mb-3">
              <label for="mood" class="form-label">Desired Mood:</label>
              <select id="mood" class="form-select" v-model="mood">
                <option value="professional">Professional</option>
                <option value="playful">Playful</option>
                <option value="sophisticated">Sophisticated</option>
                <option value="quirky">Quirky</option>
              </select>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
          <div v-if="isLoading" class="loading-spinner">
            <div class="spinner-border text-primary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </div>


          <div class="mt-5">
            <div class="alert alert-danger" role="alert" v-if="errorMessage">{{ errorMessage }}</div>
            <div class="card" v-if="designResponse">
              <div class="card-body">
                <h2 class="card-title">Design Parameters:</h2>
                <div v-for="(color, index) in designResponse.Colors" :key="index" class="d-flex align-items-center mb-3">
                  <div class="color-square me-3" :style="{ backgroundColor: color }"></div>
                  <p class="mb-0">Color {{ index + 1 }}: {{ color }}</p>
                </div>
                <p class="card-text bold">Font: {{ designResponse.Font }}</p>
                <p class="card-text bold">Justification: {{ designResponse.Justification }}</p>
                <p class="card-text bold">Project Title: {{ designResponse.Title }}</p>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      projectDescription: '',
      mood: '',
      designResponse: null,
      errorMessage: '',
      isLoading: false // Add isLoading state
    };
  },
  methods: {
    async generateDesign() {
      this.isLoading = true; // Set isLoading to true when submitting the form
      try {
        const response = await axios.post(`http://127.0.0.1:8081/api/generate_design/?text=${this.projectDescription}&mood=${this.mood}`);
        this.designResponse = response.data;
        console.log(this.designResponse);
        this.errorMessage = '';
      } catch (error) {
        this.designResponse = null;
        this.errorMessage = 'An error occurred while generating the design. Please try again later.';
      }
      this.isLoading = false; // Set isLoading to false when the response is received
    },
  },
};
</script>

<style scoped>
.loading-spinner {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px; /* set to desired height */
}


@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.bold
{
  font-weight: bold;
}

.background{
      filter: blur(0px);
      /* Full height */
      /* Center and scale the image nicely */
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      background-color:#231F20;
      color: #EEF4ED;
      height: 1080px;
      max-height: 1300px;
      border-radius: 25px;
      margin: 50px;
      padding: 50px;
  
    }

p{
  font-size: 1.2rem;
  color: #495057;
}

h2{
  font-size: 1.5rem;
  color: #495057;
}
.color-square {
  width: 30px;
  height: 30px;
  border-radius: 5px;
}

.btn-primary {
  background-color: rgb(205, 205, 205);
  border: none;
  border-radius: 10px;
  font-size: 16px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #4e4d4d;
border-color: #4e4d4d;
}

.contact_title {
color: #EEF4ED;
margin-top: 3rem;
text-align: center;
font-size: 3rem;
}

.form-group {
margin-bottom: 1rem;
}

.form-label {
display: block;
margin-bottom: 0.5rem;
font-weight: bold;
font-size: 0.9rem;
}

.form-control {
display: block;
width: 100%;
height: calc(2.25rem + 2px);
padding: 0.375rem 0.75rem;
font-size: 1rem;
font-weight: 400;
line-height: 1.5;
color: #495057;
background-color: #fff;
background-clip: padding-box;
border: 1px solid #ced4da;
border-radius: 0.25rem;
transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.textarea-control {
height: auto;
}

.select-control {
max-width: 500px;
}

.color-box {
display: flex;
align-items: center;
margin-bottom: 0.5rem;
}
.color-square {
width: 2rem;
height: 2rem;
margin-right: 0.5rem;
}

@media (max-width: 768px) {
.background {
margin: 0;
padding: 3rem;
}

.logo img {
width: 200px;
height: 200px;
right: 10%;
top: 20%;
}

.contact_title {
margin-top: 1.5rem;
font-size: 2.5rem;
}

form {
margin-left: 0;
}

.designResponse {
position: static;
margin-top: 1.5rem;
}
}

@media (max-width: 576px) {
.background {
padding: 2rem;
}

.logo img {
width: 150px;
height: 150px;
right: 5%;
top: 15%;
}

.contact_title {
margin-top: 1rem;
font-size: 2rem;
}

.form-control {
height: calc(1.5rem + 2px);
padding: 0.25rem 0.5rem;
font-size: 0.9rem;
}

.color-square {
width: 1.5rem;
height: 1.5rem;
margin-right: 0.25rem;
}
}


</style>