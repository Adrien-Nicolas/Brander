<template>
    <div>
        <div class="bg"></div>
            <div class="Content">
                <h1>
                    The new way
                    <span class="typed-text">{{ typeValue }}</span>
                    <span class="blinking-cursor">|</span>
                    <span class="cursor" :class="{ typing: typeStatus }">&nbsp;</span>
                </h1>
                <div class="profile">
                    <h3>Brander</h3>
                    <p>Think about your Brand</p>
                </div>
            </div>
    </div>
    </template>
    
    <script>
    export default {
      name: "typeWiriter",
      data: () => {
        return {
          typeValue: "",
          typeStatus: false,
          displayTextArray: ["to create your brand", "to create your identity", "to create"],
          typingSpeed: 50,
          erasingSpeed: 100,
          newTextDelay: 2000,
          displayTextArrayIndex: 0,
          charIndex: 0,
        };
      },
      props: {},
      created() {
        setTimeout(this.typeText, this.newTextDelay + 200);
      },
      methods: {
        typeText() {
          if (this.charIndex < this.displayTextArray[this.displayTextArrayIndex].length) {
            if (!this.typeStatus) this.typeStatus = true;
            this.typeValue += this.displayTextArray[this.displayTextArrayIndex].charAt(
              this.charIndex
            );
            this.charIndex += 1;
            setTimeout(this.typeText, this.typingSpeed);
          } else {
            this.typeStatus = false;
            setTimeout(this.eraseText, this.newTextDelay);
          }
        },
        eraseText() {
          if (this.charIndex > 0) {
            if (!this.typeStatus) this.typeStatus = true;
            this.typeValue = this.displayTextArray[this.displayTextArrayIndex].substring(
              0,
              this.charIndex - 1
            );
            this.charIndex -= 1;
            setTimeout(this.eraseText, this.erasingSpeed);
          } else {
            this.typeStatus = false;
            this.displayTextArrayIndex += 1;
            if (this.displayTextArrayIndex >= this.displayTextArray.length)
              this.displayTextArrayIndex = 0;
            setTimeout(this.typeText, this.typingSpeed + 1000);
          }
        },
      },
    };
    </script>
    
    
    <style scoped>
        .bg{
            filter: blur(4px);
            -webkit-filter: blur(4px);
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
            background-color: #2c3e50;
            color: #EEF4ED;
            height: 700px;
            max-height: 1000px;
        
        }
        .Content{
            background-color: rgb(0,0,0); /* Fallback color */
            background-color: rgba(0,0,0, 0.4); /* Black w/opacity/see-through */
            font-weight: bold;
            color: white;
            border-radius: 25px;
            border: 0.5px solid #a8a8a8;
            position: absolute;
            top: 400px;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 1;
            width: 40%;
            padding: 20px;
            text-align: center;
        }
    
        textarea{
            resize: both;
            max-width: 170px;
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            margin: 5px;
            padding: 10px;
            border-radius: 25px;
            background-color: #ffffff;
            color: #001742;
        }
    
    
    .blinking-cursor  
    {
       animation-duration: .8s;
       animation-name: clignoter;
       animation-iteration-count: infinite;
       transition: none;
    }
    
    @keyframes clignoter {
      0%   { opacity:1; }
      40%   {opacity:0; }
      100% { opacity:1; }
    }
    
    .profile img{
    
            height: 150px;
            border-radius: 50%;
    
        }
    </style>