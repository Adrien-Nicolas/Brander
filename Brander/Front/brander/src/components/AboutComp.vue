<template>
    <div id="about">
      <div class="background">
      <div class="grid">
        <div class="explanation">
          <h1>Presentation</h1>
          <p>
            With Brander, you can generate stunning brand proposals in just a few clicks. 
            Simply provide a project description and select your desired mood, a
            nd Brander will provide you with a range of color palettes, 
            font styles, and justification options that perfectly match your brand personality. 
            You'll be able to customize every aspect of your brand proposal, 
            from the fonts to the colors to the overall design, ensuring that your brand stands out from the crowd.
          </p>
        </div>
      </div>
      </div>
  
      </div>
    </template>
    
    <script type="text/javascript">
    export default {  
    
      }
    
      
    </script>
    
    <style scoped>
  

  
    .grid{
      display: flex;
      justify-content: center;
      align-items: center;
      flex-wrap: wrap;
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
      max-height: 900px;
      border-radius: 25px;
      margin: 50px;
      padding: 50px;
  
    }
        
    .logo img{
      position: absolute;
      top: 45%;
      left: 18%;
      transform: translate(-50%, -50%);
      width: 250px;
      height: 250px;
      border-radius: 10%;
    }
    
    .explanation{
      position: absolute;
      top: 45%;
      left: 50%;
      transform: translate(-50%, -50%);
      text-align: center;
      font-size: 15px;
      color: rgb(255, 255, 255);
      font-family: 'Auxhie';
    }
    
    .explanation h1{
      font-size: 70px;
    }
    
    .explanation p{
      font-size: 30px;
    }
    
    button{
    align-items: flex-start;
    background-color: rgb(255, 255, 255);
    border: none;
    color: rgb(0, 0, 0);
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 10px;
    cursor: pointer;
    
    }
    
    
    
    @media (max-width: 1515px) {
      .explanation{
      display: none;
      }
  
      .title{
        display: none;
    
      }
      .background{
        /**Delete background image */
        background-image: none;
      }
      .logo{
        position: absolute;
      }
  
      .description{
        position: absolute;
        top: 7%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        font-size: 30px;
        color: rgb(255, 255, 255);
        
      }
    }
  
    
  
    
    </style>