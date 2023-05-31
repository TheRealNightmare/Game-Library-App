<template>
<div class="jumbotron vertical-center">
  <div class="container">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/journal/bootstrap.min.css" integrity="sha384-QDSPDoVOoSWz2ypaRUidLmLYl4RyoBWI44iA5agn6jHegBxZkNqgm2eHb6yZ5bYs" crossorigin="anonymous">
    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center bg-primary text-white" style="border-radius:10px"> Games Library 🕹️ </h1>
        <hr><br>

        <b-alert variant="success" v-if="showMessage" show> {{ message }} </b-alert>

        <button type="button" class="btn btn-success btn-sm" v-b-modal.game-modal>Add Game</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Genre</th>
              <th scope="col">Played ?</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(game, index) in games" :key="index">
              <td>{{game.title}}</td>
              <td>{{game.genre}}</td>
              <td>
                <span v-if="game.played">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-info btn-sm"
                  v-b-modal.game-update-modal
                  @click="editGame(game)"> Update </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteGame(game)">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <Footer class="bg-primary text-white text-center" style="border-radius:10px">Enjoy!!!</Footer>

      </div>
    </div>

    <b-modal ref="addGameModal"
         id="game-modal"
         title="Add a new game" hide-backdrop
         hide-footer
         >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    <b-form-group id="form-title-group"
                  label="Title:"
                  label-for="form-title-input">
      <b-form-input id="form-title-input"
                    type="text"
                    v-model="addGameForm.title"
                    required
                    placeholder="Enter title">
      </b-form-input>
    </b-form-group>

    <b-form-group id="form-genre-group"
                  label="Genre:"
                  label-for="form-genre-input">
          <b-form-input id="form-genre-input"
                        type="text"
                        v-model="addGameForm.genre"
                        required
                        placeholder="Enter genre">
        </b-form-input>
      </b-form-group>
      
      <b-form-group id="form-played-group">
            <b-form-checkbox-group v-model="addGameForm.played" id="form-checks">
            <b-form-checkbox value="true">Played?</b-form-checkbox>
        </b-form-checkbox-group>
      </b-form-group>

      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
  </b-modal>

  <b-modal ref="editGameModal"
         id="game-update-modal"
         title="Update" hide-backdrop
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    
  <b-form-group id="form-title-edit-group"
                label="Title:"
                label-for="form-title-edit-input">
      <b-form-input id="form-title-edit-input"
                    type="text"
                    v-model="editForm.title"
                    required
                    placeholder="Enter title">
      </b-form-input>
    </b-form-group>

    <b-form-group id="form-genre-edit-group"
                  label="Genre:"
                  label-for="form-genre-edit-input">
        <b-form-input id="form-genre-edit-input"
                      type="text"
                      v-model="editForm.genre"
                      required
                      placeholder="Enter genre">
        </b-form-input>
      </b-form-group>
      
    <b-form-group id="form-played-edit-group">
      <b-form-checkbox-group v-model="editForm.played" id="form-checks">
        <b-form-checkbox value="true">Played?</b-form-checkbox>
      </b-form-checkbox-group>
    </b-form-group>

    <b-button-group>
      <b-button type="submit" variant="outline-info">Update</b-button>
      <b-button type="reset" variant="outline-danger">Cancel</b-button>
    </b-button-group>
  </b-form>
</b-modal>

  </div>
  </div>
</template>



<script>
import axios from 'axios';

export default {
  data() {
    return {
      games: [],
      addGameForm: {
        title: '',
        genre: '',
        played: [],
      },
      editForm: {
      id: '',
      title: '',
      genre: '',
      played: [],
      },
    };
  },

  message:'',

methods: {
    getGames() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.games = res.data.games;
        })
        .catch((error) => {
          console.error(error);
        });
    },

    addGame(payload) {
      const path = 'http://localhost:5000/';
      axios.post(path, payload)
        .then(() => {
          this.getGames();
          
          this.message = 'Game added 🕹️ !';
          
          this.showMessage = true;
  
        })
        .catch((error) => {
          console.log(error);
          this.getGames();
        });
    },

     initForm() {
        this.addGameForm.title = '';
        this.addGameForm.genre = '';
        this.addGameForm.played = [];
        this.editForm.id = '';
        this.editForm.title = '';
        this.editForm.genre = '';
        this.editForm.played = [];
      }, 
 
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addGameModal.hide();
      let played = false;
      if (this.addGameForm.played[0]) played = true;
      const payload = {
        title: this.addGameForm.title,
        genre: this.addGameForm.genre,
        played, 
      };
      this.addGame(payload);
      this.initForm();
    },

    onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editGameModal.hide();
    let played = false;
    if (this.editForm.played[0]) played = true;
    const payload = {
      title: this.editForm.title,
      genre: this.editForm.genre,
      played,
    };
    this.updateGame(payload, this.editForm.id);
  },

    onReset(e) {
      e.preventDefault();
      this.$refs.addGameModal.hide();
      this.initForm();
    },

updateGame(payload, gameID) {
  const path = `http://localhost:5000/${gameID}`;
  axios.put(path, payload)    
    .then(() => {
      this.getGames();
      this.message = 'Game updated ⚙️!';
      this.showMessage =  true;
    })
    .catch((error) => {
      console.error(error);
      this.getGames();
    });
},

editGame(game) {
  this.editForm = game;
},

onResetUpdate(e) {
  e.preventDefault();
  this.$refs.editGameModal.hide();
  this.initForm();
  this.getGames(); 
},

removeGame(gameID) {
  const path = `http://localhost:5000/${gameID}`;
  axios.delete(path)
    .then(() => {
      this.getGames();
      this.message = 'Game Removed 🗑️!';
      this.showMessage = true;
    })
    .catch((error) => {
      console.error(error);
      this.getGames();
    });
},

deleteGame(game) {
  this.removeGame(game.id);
},

  },
  created() {
    this.getGames(); 
  },
};
</script>