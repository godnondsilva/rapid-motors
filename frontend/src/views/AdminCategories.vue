<template>
    <div class="categories">
        <div class="container">
            <div class="heading">All Car Categories</div>
            <button class="btn btn-yellow" style="marginBottom: 20px;">
                <router-link class="rlink" to="/adminaddcategory">
                    + Add Category
                </router-link>
            </button>
            <b-table class="border-top" striped :items="items" :fields="fields">
                <template #cell(actions)="row">
                    <b-button class="button btn btn-yellow" size="sm" @click="info(row.item, row.index, $event.target)">
                        Modify
                    </b-button>
                    <b-button class="btn btn-red" size="sm" @click="row.toggleDetails">
                        Delete
                    </b-button>
                </template>
            </b-table>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    name: 'Categories',
    data() {
        return {
            fields: [
                {
                    key: 'category_id',
                    label: 'Category ID',
                    class: 'text-center',
                },
                {
                    key: 'name',
                    label: 'Category Name',
                },
                {
                    key: 'description',
                    label: 'Description',
                    thStyle: 'width: 20%'
                },
                {
                    key: 'actions',
                    label: 'Actions',
                    thStyle: 'width: 20%',
                    class: 'text-center'
                },
            ],
            items: []
        }
    },
    methods: {
        ...mapActions(['loadCategories']),
        ...mapGetters(['getCategories']),
    },
    mounted() {
        this.loadCategories()   
        this.items = this.getCategories()
    }
}
</script>

<style scoped>
.categories {
    padding: 100px 0;
}
.heading {
    font-size: 30px;
    font-weight: 600;
    margin-bottom: 20px;
}
.button {
    margin-right: 10px;
}
.btn-yellow {
    background-color: #E4C314 !important;
    color: #000 !important;
    font-weight: 600;
}
.btn-red {
    background-color: #FF918D;
    color: #000;
    font-weight: 600;
}
.rlink {
    color: #000;
    text-decoration: none;
}
</style>