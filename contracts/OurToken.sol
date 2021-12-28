// contracts/OurToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0 ;

//import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
//import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.4.0/contracts/token/ERC20/ERC20.sol";
import "./test/ERC20.sol";

contract OurToken is ERC20 {
    // wei
    constructor(uint256 initialSupply) ERC20("OurToken", "Ot") {
        _mint(msg.sender, initialSupply);
    }
}