<?php

namespace App\Http\Controllers;

use App\Models\category;
use App\Models\Member;
use App\Models\Produk;
use Illuminate\Http\Request;

class DashboardController extends Controller
{
    public function index()
    {
        $category = category::count();
        $produk = Produk::count();
        $member = Member::count();


        $tanggal_awal = date('Y-m-01');
        $tanggal_akhir = date('Y-m-d');

        $data_tanggal = array();
        $data_pendapatan = array();

        while (strtotime($tanggal_awal) <= strtotime($tanggal_akhir)) {
            $data_tanggal[] = (int) substr($tanggal_awal, 8, 2);




            $tanggal_awal = date('Y-m-d', strtotime("+1 day", strtotime($tanggal_awal)));
        }

        $tanggal_awal = date('Y-m-01');

        if (auth()->user()->level == 1) {
            return view('admin.dashboard', compact('category', 'produk', 'member',  'tanggal_awal', 'tanggal_akhir', 'data_tanggal', 'data_pendapatan'));
        } else {
            return view('kasir.dashboard');
        }
    }
}
//
