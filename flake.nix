{
  description = "nilm env";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, home-manager }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
      this-py = pkgs.python311;
      py-deps = ps: with ps; [
        pandas
      ];
      deps = with pkgs; [
        #bash

        (this-py.withPackages py-deps)
      ];
    in {
      devShells.default = pkgs.mkShell rec {
        packages = deps;
      };
    });
}
