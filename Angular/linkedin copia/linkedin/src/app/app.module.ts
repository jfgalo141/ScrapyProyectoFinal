import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { FiltrosComponent } from './comoponents/filtros/filtros.component';
import { MostrarComponent } from './comoponents/mostrar/mostrar.component';
import { InicioComponent } from './comoponents/inicio/inicio.component';
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [
    AppComponent,
    FiltrosComponent,
    MostrarComponent,
    InicioComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
