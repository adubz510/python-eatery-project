import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { thunkFetchUserCarts, thunkRemoveFromCart } from '../../redux/cart';
import './ShoppingCart.css'

function CartItem({ item, onRemove }) {
    const name = item.menuItem?.name || 'Item Name';
    const price = item.menuItem?.price || 0;
  
    return (
      <div className="cart-item">
        <span>{name}</span>
        <span>Qty: {item.quantity}</span>
        <span>Price: ${price.toFixed(2)}</span>
        <span>Subtotal: ${(price * item.quantity).toFixed(2)}</span>
        <button onClick={() => onRemove(item.id)}>Remove</button>
      </div>
    );
  }

function Cart({ cart, cartItems, onRemoveItem }) {
    const total = cartItems.reduce((sum, item) => {
        const price = item.menuItem?.price || 0;
        const quantity = item.quantity || 1;
        return sum + price * quantity;
      }, 0);

  return (
    <div className="cart">
      <h2>{cart.restaurant?.name || `Restaurant #${cart.restaurantId}`}</h2>
      {cartItems.length === 0 && <p>Cart is empty</p>}
      {cartItems.map(item => (
        <CartItem key={item.id} item={item} onRemove={onRemoveItem} />
      ))}
      <div className="cart-total">Total: ${total.toFixed(2)}</div>
    </div>
  );
}

export default function ShoppingCart() {
  const dispatch = useDispatch();
  const carts = useSelector(state => state.cart.carts);

  const cartItemsById = useSelector(state => state.cart.cartItems);

  useEffect(() => {
    dispatch(thunkFetchUserCarts());
  }, [dispatch]);

  const handleRemove = (cartItemId) => {
    dispatch(thunkRemoveFromCart(cartItemId));
  };

  if (!carts || Object.keys(carts).length === 0) {
    return <div>Your cart is empty.</div>;
  }

  return (
    <div className="shopping-cart-page">
      <h1>Your Shopping Cart</h1>
      {Object.values(carts).map(cart => {
        const items = cart.cartItems.map(id => cartItemsById[id]).filter(Boolean);
        return (
          <Cart
            key={cart.id}
            cart={cart}
            cartItems={items}
            onRemoveItem={handleRemove}
          />
        );
      })}
    </div>
  );
}