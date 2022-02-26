import { Component, OnInit } from '@angular/core';
import readXlsxFile from 'read-excel-file'

@Component({
  selector: 'app-mostrar',
  templateUrl: './mostrar.component.html',
  styleUrls: ['./mostrar.component.css']
})

export class MostrarComponent {

  private ofertas:any = '../../../../../../../scrapping/data/offerts.csv';
  //private arrayFilas:string[][];
  public jobs: csv[] = [];
  constructor(){
    
  }
}

export class csv{
  constructor(
    private titulo:string,
    public lugar: string, 
    public jornada: string,  
    public tipo: string,
  ){}

}
