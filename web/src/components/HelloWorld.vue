<template>
  <v-container class="fill-height">
  <h1> 1. Button Example </h1>
  This button has been cliceck {{button_cnt}} times.<br/><br/>
	<v-btn @click='add_button_cnt'>Add</v-btn>
  <br/>
  <br/>
  <h1> 2. Basic API Testing </h1>
	<div>
	{{api_hello}}
	</div>
  <br/>
  <h1> 3. Example of Restful API (/api/strlen/) </h1>
	<v-text-field v-model="user_input"></v-text-field>
	<v-btn @click='call_strlen'>Calculate</v-btn>
  <br/>
	<div v-if='api_strlen'>
	String length is {{api_strlen}}.
	</div>
  <br/>
  <h1> 4. Example of File Upload </h1>
	<br/>
	<v-file-input v-model="files"></v-file-input>
	<v-btn @click='upload' :disabled="files.length == 0">
	Upload
	</v-btn>
  <br/>
  <br/>
	<div v-if='api_file_size'>
	File size is {{api_file_size}}.
	</div>
  </v-container>
</template>



<script>
import axios from 'axios'
export default {
  data() {
    return {
      api_hello: "Flask Server is Not Working.",
      api_strlen: null,
      api_upload: null,
      api_file_size: null,
      button_cnt: 0,
      user_input: "",
      files: []
    }
  },
  methods: {
     add_button_cnt () {
         this.button_cnt += 1
     },
     call_strlen () {
	      axios
        .post('/api/strlen/', {input: this.user_input})
	      .then(response => (this.api_strlen = response.data.result))
     },
     upload () {
	    let formData = new FormData()
		  formData.append("file", this.files[0])
      axios.post('/api/upload/', formData,
              { headers: { 'Content-Type': 'multipart/form-data' }})
           .then( response => {
              console.log(response.data)
              this.api_file_size = response.data.result
            }).catch(error => {
                console.log({error})
            })	
     }
  },
  mounted () {
    console.log("mounted.")
    axios
      .get('/api/hello/')
      .then(response => (this.api_hello = response.data.text))
  }
}
</script>
