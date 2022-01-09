<template>
    <div class="testdrives">
        <div class="container">
            <div class="heading">All Testdrives Booked</div>
            <b-table striped class="border-top" :items="items" :fields="fields"></b-table>
        </div>
    </div>
</template>

<script>
// import { mapActions } from 'vuex'
import axios from 'axios';

export default {
    name: 'Testdrives',
    data() {
        return {
            fields: [
                {
                    key: 'testdrive_id',
                    label: 'Testdrive ID',
                    class: 'text-center',
                },
                {
                    key: 'model_id',
                    label: 'Model ID',
                    class: 'text-center',
                },
                {
                    key: 'cust_id',
                    label: 'Customer ID',
                    class: 'text-center',
                },
                {
                    key: 'testdrive_date',
                    label: 'Testdrive Date',
                    class: 'text-center',
                },
                {
                    key: 'state',
                    label: 'State',
                    class: 'text-center',
                },
                {
                    key: 'city',
                    label: 'City',
                    class: 'text-center',
                },
                {
                    key: 'comments',
                    label: 'Comments',
                    thStyle: 'width: 40%; text-align: center;',
                }
            ],
            items: []
        }
    },
    methods: {
        async loadAdminTestdrives() {
            await axios.get('http://localhost:5000/admintestdrives')
            .then((response) => {
                this.items = response.data
            })
        },
    },
    mounted() {
        this.loadAdminTestdrives()    
    }
}
</script>

<style scoped>
.testdrives {
    padding: 100px 0;
}
.heading {
    font-size: 30px;
    font-weight: 600;
    margin-bottom: 50px;
}
</style>