<template>
  <v-container class="fill-height">
<!--
	<div v-if='api'>
	{{api.text}}
	</div>
	<div v-else>
	{{text}}
	</div>
	<v-text-field label="Regular" v-model="user_input">
        </v-text-field>
	<v-btn elevation="2" @click='clicked'>
		Hello, Button!
	</v-btn>
	<div v-if='api'>
	Response from Python: {{api.result}}
	</div>
-->

	<br/>
	<v-file-input
	  truncate-length="15" v-model="files"
	></v-file-input>
	<v-btn elevation="2" @click='upload'>
	Upload
	</v-btn>

  </v-container>
</template>



<script>
import axios from 'axios'
export default {
  data() {
    return {
      text: "Hello from Vue!",
      api: null,
      cnt: 0,
      user_input: "",
      sum: "",
      files: [],
    }
  },
  methods: {
     clicked () {
	//alert(this.user_input)
	//console.log("Clicked!" + this.cnt)
	//console.log(this.user_input)
	//this.sum = (+this.user_input) + (+this.user_input2)
	//this.cnt += 1
	    axios
              .post('/api/strlen/', {input: this.user_input})
	      .then(response => (this.api = response.data))
     },
     upload () {
	    let formData = new FormData()
	    for (let file in this.files) {
		formData.append("something", file)
	    }
            axios.post('/api/upload/',
                        {
                            files: formData,
                        }, 
                        { 
                            headers: { 
                                'Content-Type': 'multipart/form-data'
                            } 
                        }).then( response => {
                            console.log('Success!')
                            console.log({response})
                        }).catch(error => {
                            console.log({error})
                        })	
     }
  },
  mounted () {
    console.log("mounted.")
	  /*
    axios
      .get('/api/hello/')
      .then(response => (this.api = response.data))
      */
  }
}
</script>
