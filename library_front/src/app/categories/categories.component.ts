import {Component, OnInit} from '@angular/core';
import {CategoryService} from "../services/category/category.service";
import {Category} from "../../models/Category";
import {LoginService} from "../services/login/login.service";

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css']
})
export class CategoriesComponent implements OnInit{
  logged:boolean = false;
  categories:Category[] = []
  ngOnInit(): void {
    this.loginService.isAuthenticated().subscribe((data) =>{
      this.logged = data;
    })
    if(this.logged){
      this.getCategories();
    }
  }
  getCategories(){
    this.categoryService.getCategories().subscribe( (categories) => {
      this.categories =categories;
    });
  }
  constructor(private categoryService:CategoryService, private loginService: LoginService) {
  }

}
