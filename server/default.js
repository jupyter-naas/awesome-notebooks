

import Product from './model/productSchema.js';
import { products } from './constants/product.js';

const DefaultData = async () => {
    try {
        products.deleteMany();
        products.insertMany({Product})

        console.log('Data imported Successfully');
        
    } catch (error) {
        console.log('Error: ', error.message);
    }
}

export default DefaultData;