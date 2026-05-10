{
  description = "Minimal dev shell";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          pkgs.python314
          pkgs.python314Packages.numpy
          pkgs.python314Packages.scipy
          pkgs.python314Packages.matplotlib
          pkgs.python314Packages.requests
          pkgs.python314Packages.pandas
          pkgs.python314Packages.seaborn
          ];
        shellHook = ''
          echo "Welcome to the devShell!"
        '';
      };
    };
}
