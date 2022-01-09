<template>
    <div class="forgot-password">
        <div class="forgot-password-form">
            <div class="forgot-password-form-header">
                Forgot your password? Don't worry!
            </div>
            <div class="forgot-password-form-body">
                <validation-observer v-slot="{ invalid, handleSubmit }">
                    <form @submit.prevent="handleSubmit(forgotPassword)">
                        <div class="form-group">
                            <p>If you have forgotten your password, we can send you your password to your registered email address.</p>
                            <p>Please enter your email address below so that we can send you your password.</p>
                        </div>
                        <div class="form-group">
                            <label for="email">Email</label>
                            <validation-provider rules="required|email|max:30" v-slot="{ errors }">
                                <input type="email" id="email" v-model="email" placeholder="Enter your email">
                                <div class="text-danger push-right">{{ errors[0] }}</div>
                            </validation-provider>
                        </div>
                        <b-button @click="show=true" type="submit" class="btn-bg btn-yellow push-right" :disabled="invalid">Send</b-button>
                        <div class="bottom-question">
                            <router-link class="router-link" to="/login">Go back to login page</router-link>
                        </div>
                
                        <b-modal v-model="show" id="forgot-password" type="submit" :title="forgotPasswordFormHeader">
                            <p class="my-4">{{ forgotPasswordFormText }} </p>
                            <template #modal-footer>
                                <b-button
                                    size="md"
                                    class="float-right btn-yellow"
                                    @click="show=false"
                                >
                                    OK
                                </b-button>
                            </template>
                        </b-modal>
                    </form>
                </validation-observer>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { ValidationProvider, ValidationObserver  } from 'vee-validate';

export default {
    name: 'ForgotPassword',
    data() {
        return {
            email: '',
            forgotPasswordFormHeader: 'Verifying your email address..',
            forgotPasswordFormText: 'Please wait while we are verifying your information',
            shouldRoute: false,
            show: false,
        }
    },
    components: {
        ValidationObserver,
        ValidationProvider,
    },
    methods: {
        async forgotPassword() {
            const data = {
                email: this.email,
            }
            await axios.post('http://localhost:5000/forgotpassword', data, {
                headers: {
                'Content-Type': 'application/json'
                },
            })
            .then((response) => {
                console.log(response)
                if(response.data.message) {
                    this.forgotPasswordFormHeader = 'Success!';
                    this.forgotPasswordFormText = 'Email has been sent!';
                    this.shouldRoute = true;
                }
                // error case
                else if (response.data.error === 'User not found') {
                    this.forgotPasswordFormHeader = 'Error!';
                    this.forgotPasswordFormText = 'There exists no account for the given email.';
                }
                else {
                    this.forgotPasswordFormHeader = 'Error!';
                    this.forgotPasswordFormText = 'An error has occured. Please try again later.';
                }
            })
            .catch(() => {
                this.forgotPasswordFormHeader = 'Error!';
                this.forgotPasswordFormText = 'Something went wrong!';
            })
        }
    }
}
</script>

<style scoped>
.forgot-password {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 50px 0 100px 0;
}
.forgot-password-form {
    background-color: #F5F5F5;
    padding: 50px 200px;
}
.forgot-password-form-header {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 50px;
    text-align: center;
}
.forgot-password-form-error {
    padding: 10px 0;
    color: #fff;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 50px;
    text-align: center;
}
label {
    width: 150px;
    font-weight: 500;
}
.form-group {
    margin-bottom: 30px;
}
input {
    width: 400px;
    height: 35px;
    border: 1px solid #eee;
    padding: 0 10px;
}
textarea {
    width: 600px;
    height: 100px;
    border: 1px solid #eee;
    padding: 10px;
    resize: none;
}
.textarea-label {
    vertical-align: top;
}
.btn-yellow {
    background-color: #E4C314 !important;
    color: #000 !important;
    margin-left: 150px;
    font-weight: 600;
}
.btn-yellow:disabled {
    background-color: #666 !important;
    color: #fff !important;
}
.bottom-question {
    padding-top: 27px;
    margin-left: 150px;
}
.push-right {
    margin-left: 150px;
}
</style>