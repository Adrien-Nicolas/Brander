<template>
  <Landing/>
  <AboutComp/>
  
  <HelloWorld/>
  <FooterComp/>

</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Landing from './components/Landing.vue';
import FooterComp from './components/FooterComp.vue';
import AboutComp from './components/AboutComp.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
    Landing,
    AboutComp,
    FooterComp
    
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0px;
  overflow-x: hidden;
  background-color: #231F20;
}
</style>
