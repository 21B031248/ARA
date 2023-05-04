import {Component, OnInit} from '@angular/core';
import {CategoryService} from "../services/category/category.service";
import {UserService} from "../services/user/user.service";
import {CartService} from "../services/cart/cart.service";
import {Cart} from "../../models/Cart";
import {Product} from "../../models/Product";
import {User} from "../../models/User";
import {LoginService} from "../services/login/login.service";

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {
  constructor(private cartService: CartService, private userService: UserService,
              private categoryService: CategoryService, private loginService: LoginService) {
  }

  cart!: Cart;
  cartProducts: Product [] = [];
  user_id!: number;
  user!: User;
  logged: boolean = false;
  ngOnInit() {
    this.loginService.isAuthenticated().subscribe((data)=>{
      this.logged = data;
    })
    this.userService.get_id().subscribe((data) => {
      this.user_id = data.user_id;
      if (this.user_id) {
        this.getCart();
      }
    })
  }

  getCart() {
    this.cartService.getCart(this.user_id).subscribe((data) => {
      this.cart = data;
      this.user = data.user;
      this.cartProducts = data.books;
    })
  }

  remove(product_id: number) {
    this.cartService.removeFromCart(product_id).subscribe((data) => {
      this.cartProducts = this.cartProducts.filter((product) => product.id !== product_id);
    })
  }

}
