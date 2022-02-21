import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MostrarComponent } from './comoponents/mostrar/mostrar.component';
import { InicioComponent } from './comoponents/inicio/inicio.component';
import { FiltrosComponent } from './comoponents/filtros/filtros.component';
const routes: Routes = [
  { path: 'mostrar', component: MostrarComponent },
  { path: 'inicio', component: InicioComponent },
  { path: 'filtro', component: FiltrosComponent },
  { path: '', redirectTo: '/inicio', pathMatch: 'full' },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
