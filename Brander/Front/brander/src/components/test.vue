<template>
    <div>
      <div class="background">
            <form @submit.prevent="generateDesign">
            <label for="project-description">Project Description:</label>
            <textarea id="project-description" v-model="projectDescription"></textarea>
            <label for="mood">Desired Mood:</label>
            <select id="mood" v-model="mood">
              <option value="professional">Professional</option>
              <option value="playful">Playful</option>
              <option value="sophisticated">Sophisticated</option>
              <option value="quirky">Quirky</option>
            </select>
            <button type="submit">Submit</button>
          </form>
          <div v-if="errorMessage" style="color: red">{{ errorMessage }}</div>
          <div v-if="designResponse">
            <h2>Design Parameters:</h2>
            <div v-for="(color, index) in designResponse.Colors" :key="index" class="color-box">
              <div class="color-square" :style="{ backgroundColor: color }"></div>
              <p>Color {{ index + 1 }}: {{ color }}</p>
            </div>
            <p>Font: {{ designResponse.Font }}</p>
            <p>Justification: {{ designResponse.Justification}}</p>
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
      };
    },
    methods: {
    async generateDesign() {
      try {
        const response = await axios.post(`http://127.0.0.1:8082/api/generate_design/?text=${this.projectDescription}&mood=${this.mood}`);
        this.designResponse = response.data;
        console.log(this.designResponse);
        this.errorMessage = '';
      } catch (error) {
        this.designResponse = null;
        this.errorMessage = 'An error occurred while generating the design. Please try again later.';
      }
    },
  },
  };
  </script>
  
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
    .grid{
      display: flex;
      justify-content: center;
      align-items: center;
      flex-wrap: wrap;
    }
    .title {
      position: absolute;
      left: 10%;
      
  
      
    }
  
    body {
      background-color: #F1FAEE;
      color: #011627;
      font-family: 'Open Sans', sans-serif;
    }
    header {
      background-color: #1D3557;
      color: #F1FAEE;
      padding: 20px;
    }
    nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    nav a {
      color: #F1FAEE;
      text-decoration: none;
      margin-right: 20px;
    }
    .background {
              /* background-image: url('../assets/pdp.jpg'); */
              /* Full height */
              /* Center and scale the image nicely */ 
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;
      margin: 50px;
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      padding: 50px;
      border-radius: 25px;
      background-color: #092a46;
      color: #EEF4ED;
      height: 700px;
      max-height: 1000px;
    }
  
    .color-square {
          display: inline-block;
          width: 20px;
          height: 20px;
          margin-right: 10px;
          border: 1px solid #011627;
        }
        .color-box {
          display: flex;
          align-items: center;
          margin-bottom: 5px;
        }
  
  </style> 