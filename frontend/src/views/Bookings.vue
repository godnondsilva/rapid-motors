<template>
	<div class="bookings">
		<div class="container">
			<div class="heading">Cars Booked</div>
			<b-table
				class="border-top"
				striped
				:items="items"
				:fields="fields"
			></b-table>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'Bookings',
	data() {
		return {
			fields: [
				{
					key: 'booking_id',
					label: 'Booking ID',
					class: 'text-center',
				},
				{
					key: 'model_id',
					label: 'Model ID',
					class: 'text-center',
				},
				{
					key: 'booking_date',
					label: 'Booking Date',
					class: 'text-center',
				},
				{
					key: 'name',
					label: 'Model Name',
					class: 'text-center',
				},
				{
					key: 'booking_color',
					label: 'Color',
					class: 'text-center',
				},
				{
					key: 'booking_price',
					label: 'Booking Price',
					class: 'text-center',
				},
			],
			items: [],
		};
	},
	methods: {
		async loadCustBookings() {
			await axios
				.get(`http://localhost:5000/bookings/${this.$route.params.cust_id}`)
				.then((response) => {
					this.items = response.data;
				});
		},
	},
	mounted() {
		this.loadCustBookings();
	},
};
</script>

<style scoped>
.bookings {
	padding: 100px 0;
}
.heading {
	font-size: 30px;
	font-weight: 600;
	margin-bottom: 50px;
}
</style>
