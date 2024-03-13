import React from 'react';
import { styled } from '@mui/system';
import {Link} from 'react-router-dom'
import flipImage from './flip.jpg'
const CardContainer = styled('div')({
  border: '1px solid #ccc',
  padding:10,
  margin: 0,
  width: 'calc(50% )', // Adjust the width based on your design
  boxSizing: 'border-box',
  textAlign: 'left',
  display: 'inline-block',
  verticalAlign: 'top',
  backgroundColor: '#ffffff', // Light gray background color
});

const ProductImage = styled('img')({
  width: 144,
  height: 150,
  marginBottom: 10,
  textAlign:"center"
});

const Title = styled('p')({
  overflow: 'hidden',
  textOverflow: 'ellipsis',
  whiteSpace: 'nowrap',
  color: 'black',
  fontWeight:'bold'
});
const Des = styled('p')({
  overflow: 'hidden',
  textOverflow: 'ellipsis',
  whiteSpace: 'nowrap',
  color: '#818589',
  fontSize:15
});

const Discount = styled('span')({
  color: 'green',
  fontSize: '12.5px',
  marginBottom: 10,
  fontWeight:'bold'
});

const Price = styled('span')({
  fontSize: '14px',
  color: 'black',
  fontWeight: 'bold', // Make the price bold
});

const Pric = styled('span')({
  fontSize: '12px',
  color: 'black',
});

const Pr = styled('span')({
  fontSize: '12.5px',
  marginBottom: 10,
  color: 'black',
});
const Bol=styled('span')({
  color: 'green',
  fontSize: '20px',
  fontWeight:"bold",
  marginBottom: 10,
})

const ProductCard = ({ title, price, discount, url, pr,_id }) => {
  return (
    <>
    <Link to={`product/${_id}`}>
    <CardContainer>
      <ProductImage src={url} alt={title} />
      <Title>{title.shortTitle}</Title>
      <Des>{title.longTitle}</Des>
      <Discount><Bol>↓</Bol>{price.discount} </Discount>
      <Pr><del>₹{price.mrp} </del></Pr>
      <Price>₹{price.cost}</Price>
      <br />
      <Discount>★★★★☆</Discount>
      <img src={flipImage} alt="Flip Image" style={{ width: 70, height: 20 }} />
      <br/>
      <Pric>Free Delivery in 2 Days</Pric>
    </CardContainer>
    </Link>
    </>
  );
};

export default ProductCard;